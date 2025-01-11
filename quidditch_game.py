from flask import Flask, request, jsonify, render_template_string, session, redirect, url_for, send_file
from werkzeug.security import generate_password_hash, check_password_hash
import random
import os

app = Flask(__name__)
app.secret_key = 'quidditch_secret_key'

# User data (predefined by master)
users = {
    "master": {
        "password": generate_password_hash("masterpass"),
        "role": "master"
    },
    "player1": {
        "password": generate_password_hash("player1pass"),
        "role": "chaser"
    },
    "player2": {
        "password": generate_password_hash("player2pass"),
        "role": "chaser"
    },
    "player3": {
        "password": generate_password_hash("player3pass"),
        "role": "chaser"
    },
    "player4": {
        "password": generate_password_hash("player4pass"),
        "role": "keeper"
    },
    "player5": {
        "password": generate_password_hash("player5pass"),
        "role": "beater"
    },
    "player6": {
        "password": generate_password_hash("player6pass"),
        "role": "beater"
    },
    "player7": {
        "password": generate_password_hash("player7pass"),
        "role": "seeker"
    },
    "player8": {
        "password": generate_password_hash("player8pass"),
        "role": "chaser"
    },
    "player9": {
        "password": generate_password_hash("player9pass"),
        "role": "chaser"
    },
    "player10": {
        "password": generate_password_hash("player10pass"),
        "role": "chaser"
    },
    "player11": {
        "password": generate_password_hash("player11pass"),
        "role": "keeper"
    },
    "player12": {
        "password": generate_password_hash("player12pass"),
        "role": "beater"
    },
    "player13": {
        "password": generate_password_hash("player13pass"),
        "role": "beater"
    },
    "player14": {
        "password": generate_password_hash("player14pass"),
        "role": "seeker"
    }
}

# Game state
teams = {
    "team_1": {
        "players": [],
        "score": 0
    },
    "team_2": {
        "players": [],
        "score": 0
    }
}
quaffle_possession = "team_1"
snitch_caught = False
current_event = ""
game_started = False
chat_history = []
chat_file = "chat_history.txt"

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
    <a href="/commentator">Watch as Commentator</a>
    {% if error %}
    <p style="color: red;">{{ error }}</p>
    {% endif %}
</body>
</html>
"""

game_template_master = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Master Controls</title>
</head>
<body>
    <h1>Quidditch Game Master Controls</h1>
    <form action="/start_game" method="post">
        <button type="submit">Start Game</button>
    </form>
    <form action="/download_chat" method="post">
        <button type="submit">Download Chat History</button>
    </form>
    <form action="/end_game" method="post">
        <button type="submit">End Game</button>
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
</head>
<body>
    <h1>Welcome {{ session['username'] }}</h1>
    <h2>Role: {{ role }}</h2>
    <h3>Team 1 Score: {{ teams['team_1']['score'] }}</h3>
    <h3>Team 2 Score: {{ teams['team_2']['score'] }}</h3>
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
        <p>Waiting for the master to start the game...</p>
    {% endif %}
    <h3>Chat</h3>
    <div style="border: 1px solid #000; padding: 10px; height: 300px; overflow-y: scroll;">
        {% for message in chat_history %}
            <p>{{ message }}</p>
        {% endfor %}
    </div>
    <form action="/send_message" method="post">
        <input type="text" name="message" placeholder="Enter your message" required>
        <button type="submit">Send</button>
    </form>
</body>
</html>
"""

def save_chat_history():
    with open(chat_file, "w") as f:
        f.write("\n".join(chat_history))

@app.route("/", methods=["GET"])
def index():
    if "username" not in session:
        return redirect(url_for("login"))
    
    username = session["username"]
    user = users.get(username)

    if not user:
        session.pop("username", None)
        return redirect(url_for("login"))

    if username == "master":
        return render_template_string(game_template_master)

    return render_template_string(
        game_template_player, 
        teams=teams, 
        chat_history=chat_history, 
        game_started=game_started, 
        role=user["role"]
    )

@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = users.get(username)
        if user and check_password_hash(user["password"], password):
            session["username"] = username
            return redirect(url_for("index"))
        else:
            error = "Invalid username or password."
    return render_template_string(login_template, error=error)

@app.route("/logout", methods=["POST"])
def logout():
    session.pop("username", None)
    return redirect(url_for("login"))

@app.route("/start_game", methods=["POST"])
def start_game():
    if "username" in session and session["username"] == "master":
        global game_started
        game_started = True
    return redirect(url_for("index"))

@app.route("/end_game", methods=["POST"])
def end_game():
    if "username" in session and session["username"] == "master":
        global game_started, chat_history, teams, quaffle_possession, snitch_caught
        game_started = False
        chat_history = []
        teams["team_1"]["score"] = 0
        teams["team_2"]["score"] = 0
        quaffle_possession = "team_1"
        snitch_caught = False
        if os.path.exists(chat_file):
            os.remove(chat_file)
    return redirect(url_for("index"))

@app.route("/download_chat", methods=["POST"])
def download_chat():
    if "username" in session and session["username"] == "master":
        save_chat_history()
        return send_file(chat_file, as_attachment=True)
    return redirect(url_for("index"))

@app.route("/action", methods=["POST"])
def action():
    if "username" not in session or not game_started:
                return redirect(url_for("index"))

    action = request.form.get("action")

    chat_history.append(f"{session['username']} performed action: {action}")

    return redirect(url_for("index"))



@app.route("/send_message", methods=["POST"])

def send_message():

    if "username" not in session:

        return redirect(url_for("index"))

    message = request.form.get("message")

    chat_history.append(f"{session['username']}: {message}")

    return redirect(url_for("index"))



@app.route("/commentator", methods=["GET"])

def commentator():

    return render_template_string(game_template_player, teams=teams, chat_history=chat_history, game_started=game_started, role="commentator")



if __name__ == "__main__":

    app.run(debug=True)