from flask import Flask, request, jsonify, render_template_string, session, redirect, url_for, send_file
from werkzeug.security import generate_password_hash, check_password_hash
import random
import os

app = Flask(__name__)
app.secret_key = 'quidditch_secret_key'

# User data (predefined by referee)
users = {
    "referee": {
        "password": generate_password_hash("refereepass"),
        "role": "referee"
    },
    **{f"player{i}": {"password": generate_password_hash(f"player{i}pass"), "role": role} for i, role in enumerate(
        ["chaser", "chaser", "chaser", "keeper", "beater", "beater", "seeker"] * 4, start=1)
    }
}

# Game state
teams = {
    "team_1": {
        "players": [f"player{i}" for i in range(1, 8)],
        "score": 0
    },
    "team_2": {
        "players": [f"player{i}" for i in range(8, 15)],
        "score": 0
    },
    "team_3": {
        "players": [f"player{i}" for i in range(15, 22)],
        "score": 0
    },
    "team_4": {
        "players": [f"player{i}" for i in range(22, 29)],
        "score": 0
    }
}
quaffle_possession = "team_1"
snitch_caught = False
current_event = ""
game_started = False
chat_history = []
chat_file = "chat_history.txt"
selected_teams = []

# HTML templates
login_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
</head>
<body>
    <h1>Login</h1>
    <form action="/login" method="post">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required><br><br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required><br><br>
        <button type="submit">Login</button>
    </form>
    <br>
    <a href="/spectator">Watch as Spectator</a>
    {% if error %}
    <p style="color: red;">{{ error }}</p>
    {% endif %}
</body>
</html>
"""

game_template_referee = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Referee Controls</title>
</head>
<body>
    <h1>Quidditch Game Referee Controls</h1>
    <form action="/select_teams" method="post">
        <label for="team1">Select Team 1:</label>
        <select name="team1" id="team1">
            {% for team in teams.keys() %}
            <option value="{{ team }}">{{ team }}</option>
            {% endfor %}
        </select>
        <label for="team2">Select Team 2:</label>
        <select name="team2" id="team2">
            {% for team in teams.keys() %}
            <option value="{{ team }}">{{ team }}</option>
            {% endfor %}
        </select>
        <button type="submit">Set Match</button>
    </form>
    <form action="/start_game" method="post">
        <button type="submit">Start Game</button>
    </form>
    <form action="/download_chat" method="post">
        <button type="submit">Download Chat History</button>
    </form>
    <form action="/end_game" method="post">
        <button type="submit">End Game</button>
    </form>
    <h3>Chat</h3>
    <div id="chat-box" style="border: 1px solid #000; padding: 10px; height: 300px; overflow-y: scroll;">
        {% for message in chat_history %}
            <p>{{ message }}</p>
        {% endfor %}
    </div>
    <form action="/send_message" method="post">
        <input type="text" name="message" placeholder="Enter your message" required style="width: 90%;">
        <button type="submit">Send</button>
    </form>
</body>
</html>
"""

game_template_player = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Quidditch Game</title>
    <script>
        function updateChat() {
            fetch('/get_chat')
                .then(response => response.json())
                .then(data => {
                    const chatBox = document.getElementById('chat-box');
                    chatBox.innerHTML = data.chat_history.map(msg => `<p>${msg}</p>`).join('');
                });
        }
        setInterval(updateChat, 2000);
    </script>
</head>
<body>
    {% if role != 'spectator' %}
        <h1>Welcome {{ session['username'] }}</h1>
        <h2>Role: {{ role }}
    {% else %}
        <h1>Welcome Spectator</h1>
        <h2>Role: {{ role }}</h2>
    {% endif %}
    {% if selected_teams %}
        <h3>Team 1 Score: {{ teams[selected_teams[0]]['score'] }}</h3>
        <h3>Team 2 Score: {{ teams[selected_teams[1]]['score'] }}</h3>
    {% endif %}
    {% if game_started %}
        <form action="/action" method="post">
            {% if role == 'chaser' %}
                <button name="action" value="catch_quaffle">Catch Quaffle</button>
                <button name="action" value="pass_quaffle">Pass Quaffle</button>
            {% elif role == 'keeper' %}
                <button name="action" value="block_goal">Block Goal</button>
            {% elif role == 'beater' %}
                <button name="action" value="hit_bludger">Hit Bludger</button>
            {% elif role == 'seeker' %}
                <button name="action" value="catch_snitch">Catch Snitch</button>
            {% endif %}
        </form>
    {% else %}
        <p>Waiting for the referee to start the game...</p>
    {% endif %}
    <h3>Chat</h3>
    <div id="chat-box" style="border: 1px solid #000; padding: 10px; height: 300px; overflow-y: scroll;">
        {% for message in chat_history %}
            <p>{{ message }}</p>
        {% endfor %}
    </div>
    {% if role != 'spectator' and session['username'] in teams[selected_teams[0]]['players'] + teams[selected_teams[1]]['players'] %}
    <form action="/send_message" method="post">
        <input type="text" name="message" placeholder="Enter your message" required style="width: 90%;">
        <button type="submit">Send</button>
    </form>
    {% endif %}
</body>
</html>
"""

def save_chat_history():
    with open(chat_file, "w") as f:
        f.write("\n".join(chat_history))

@app.route("/", methods=["GET"])
def index():
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = users.get(username)
        if user and check_password_hash(user["password"], password):
            session["username"] = username
            return redirect(url_for("dashboard"))
        else:
            error = "Invalid username or password."
    return render_template_string(login_template, error=error)

@app.route("/dashboard", methods=["GET"])
def dashboard():
    if "username" not in session:
        return redirect(url_for("login"))

    username = session["username"]
    user = users.get(username)

    if not user:
        session.pop("username", None)
        return redirect(url_for("login"))

    if username == "referee":
        return render_template_string(game_template_referee, chat_history=chat_history, teams=teams)

    return render_template_string(
        game_template_player, 
        teams=teams, 
        chat_history=chat_history, 
        game_started=game_started, 
        role=user["role"],
        selected_teams=selected_teams
    )

@app.route("/logout", methods=["POST"])
def logout():
    session.pop("username", None)
    return redirect(url_for("login"))

@app.route("/start_game", methods=["POST"])
def start_game():
    if "username" in session and session["username"] == "referee" and len(selected_teams) == 2:
        global game_started
        game_started = True
    return redirect(url_for("dashboard"))

@app.route("/end_game", methods=["POST"])
def end_game():
    if "username" in session and session["username"] == "referee":
        global game_started, chat_history, quaffle_possession, snitch_caught, selected_teams
        game_started = False
        chat_history = []
        quaffle_possession = "team_1"
        snitch_caught = False
        selected_teams = []
        if os.path.exists(chat_file):
            os.remove(chat_file)
    return redirect(url_for("dashboard"))

@app.route("/download_chat", methods=["POST"])
def download_chat():
    if "username" in session and session["username"] == "referee":
        save_chat_history()
        return send_file(chat_file, as_attachment=True)
    return redirect(url_for("dashboard"))

@app.route("/action", methods=["POST"])
def action():
    if "username" not in session or not game_started:
        return redirect(url_for("dashboard"))

    action = request.form.get("action")

    chat_history.append(f"{session['username']} performed action: {action}")

    return redirect(url_for("dashboard"))

@app.route("/send_message", methods=["POST"])
def send_message():
    if session["username"] != "referee":
        if "username" not in session or session["username"] not in teams[selected_teams[0]]['players'] + teams[selected_teams[1]]['players']:
            return redirect(url_for("dashboard"))
    
    print(session["username"])
    message = request.form.get("message")

    chat_history.append(f"{session['username']}: {message}")

    return redirect(url_for("dashboard"))

@app.route("/spectator", methods=["GET"])
def spectator():
    if "spectator_id" not in session:
        session["spectator_id"] = "Spectator"
    spectator_name = session["spectator_id"]
    return render_template_string(game_template_player, teams=teams, chat_history=chat_history, game_started=game_started, role="spectator", selected_teams=selected_teams)

@app.route("/get_chat", methods=["GET"])
def get_chat():
    return jsonify({"chat_history": chat_history})

@app.route("/select_teams", methods=["POST"])
def select_teams():
    if "username" in session and session["username"] == "referee":
        team1 = request.form.get("team1")
        team2 = request.form.get("team2")

        # Validate that both teams are selected and not the same
        if team1 and team2 and team1 in teams and team2 in teams and team1 != team2:
            global selected_teams
            selected_teams = [team1, team2]
            chat_history.append(f"Referee has selected {team1} and {team2} for the match.")
        else:
            chat_history.append("Invalid team selection. Please select two different teams.")

    return redirect(url_for("dashboard"))

if __name__ == "__main__":
    app.run(debug=True)