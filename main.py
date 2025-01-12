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
    "player1": {
        "password": generate_password_hash("player1pass"),
        "role": "chaser",
        "skills": {
            "accuracy": 0.1,
            "handling": 0.1,
            "defense": 0.1,
            "agility": 0.1,
            "strength": 0.1,
            "morale": 0.1,
        }
    },
    "player2": {
        "password": generate_password_hash("player2pass"),
        "role": "chaser",
        "skills": {
            "accuracy": 0.1,
            "handling": 0.1,
            "defense": 0.1,
            "agility": 0.1,
            "strength": 0.1,
            "morale": 0.1,
        }
    },
    "player3": {
        "password": generate_password_hash("player3pass"),
        "role": "chaser",
        "skills": {
            "accuracy": 0.1,
            "handling": 0.1,
            "defense": 0.1,
            "agility": 0.1,
            "strength": 0.1,
            "morale": 0.1,
        }
    },
    "player4": {
        "password": generate_password_hash("player4pass"),
        "role": "keeper",
        "skills": {
            "accuracy": 0.1,
            "handling": 0.1,
            "defense": 0.1,
            "agility": 0.1,
            "strength": 0.1,
            "morale": 0.1,
        }
    },
    "player5": {
        "password": generate_password_hash("player5pass"),
        "role": "beater",
        "skills": {
            "accuracy": 0.1,
            "handling": 0.1,
            "defense": 0.1,
            "agility": 0.1,
            "strength": 0.1,
            "morale": 0.1,
        }
    },
    "player6": {
        "password": generate_password_hash("player6pass"),
        "role": "beater",
        "skills": {
            "accuracy": 0.1,
            "handling": 0.1,
            "defense": 0.1,
            "agility": 0.1,
            "strength": 0.1,
            "morale": 0.1,
        }
    },
    "player7": {
        "password": generate_password_hash("player7pass"),
        "role": "seeker",
        "skills": {
            "accuracy": 0.1,
            "handling": 0.1,
            "defense": 0.1,
            "agility": 0.1,
            "strength": 0.1,
            "morale": 0.1,
        }
    },
    "player8": {
        "password": generate_password_hash("player8pass"),
        "role": "chaser",
        "skills": {
            "accuracy": 0.1,
            "handling": 0.1,
            "defense": 0.1,
            "agility": 0.1,
            "strength": 0.1,
            "morale": 0.1,
        }
    },
    "player9": {
        "password": generate_password_hash("player9pass"),
        "role": "chaser",
        "skills": {
            "accuracy": 0.1,
            "handling": 0.1,
            "defense": 0.1,
            "agility": 0.1,
            "strength": 0.1,
            "morale": 0.1,
        }
    },
    "player10": {
        "password": generate_password_hash("player10pass"),
        "role": "chaser",
        "skills": {
            "accuracy": 0.1,
            "handling": 0.1,
            "defense": 0.1,
            "agility": 0.1,
            "strength": 0.1,
            "morale": 0.1,
        }
    },
    "player11": {
        "password": generate_password_hash("player11pass"),
        "role": "keeper",
        "skills": {
            "accuracy": 0.1,
            "handling": 0.1,
            "defense": 0.1,
            "agility": 0.1,
            "strength": 0.1,
            "morale": 0.1,
        }
    },
    "player12": {
        "password": generate_password_hash("player12pass"),
        "role": "beater",
        "skills": {
            "accuracy": 0.1,
            "handling": 0.1,
            "defense": 0.1,
            "agility": 0.1,
            "strength": 0.1,
            "morale": 0.1,
        }
    },
    "player13": {
        "password": generate_password_hash("player13pass"),
        "role": "beater",
        "skills": {
            "accuracy": 0.1,
            "handling": 0.1,
            "defense": 0.1,
            "agility": 0.1,
            "strength": 0.1,
            "morale": 0.1,
        }
    },
    "player14": {
        "password": generate_password_hash("player14pass"),
        "role": "seeker",
        "skills": {
            "accuracy": 0.1,
            "handling": 0.1,
            "defense": 0.1,
            "agility": 0.1,
            "strength": 0.1,
            "morale": 0.1,
        }
    },
    "player15": {
        "password": generate_password_hash("player15pass"),
        "role": "chaser",
        "skills": {
            "accuracy": 0.1,
            "handling": 0.1,
            "defense": 0.1,
            "agility": 0.1,
            "strength": 0.1,
            "morale": 0.1,
        }
    },
    "player16": {
        "password": generate_password_hash("player16pass"),
        "role": "chaser",
        "skills": {
            "accuracy": 0.1,
            "handling": 0.1,
            "defense": 0.1,
            "agility": 0.1,
            "strength": 0.1,
            "morale": 0.1,
        }
    },
    "player17": {
        "password": generate_password_hash("player17pass"),
        "role": "chaser",
        "skills": {
            "accuracy": 0.1,
            "handling": 0.1,
            "defense": 0.1,
            "agility": 0.1,
            "strength": 0.1,
            "morale": 0.1,
        }
    },
    "player18": {
        "password": generate_password_hash("player18pass"),
        "role": "keeper",
        "skills": {
            "accuracy": 0.1,
            "handling": 0.1,
            "defense": 0.1,
            "agility": 0.1,
            "strength": 0.1,
            "morale": 0.1,
        }
    },
    "player19": {
        "password": generate_password_hash("player19pass"),
        "role": "beater",
        "skills": {
            "accuracy": 0.1,
            "handling": 0.1,
            "defense": 0.1,
            "agility": 0.1,
            "strength": 0.1,
            "morale": 0.1,
        }
    },
    "player20": {
        "password": generate_password_hash("player20pass"),
        "role": "beater",
        "skills": {
            "accuracy": 0.1,
            "handling": 0.1,
            "defense": 0.1,
            "agility": 0.1,
            "strength": 0.1,
            "morale": 0.1,
        }
    },
    "player21": {
        "password": generate_password_hash("player21pass"),
        "role": "seeker",
        "skills": {
            "accuracy": 0.1,
            "handling": 0.1,
            "defense": 0.1,
            "agility": 0.1,
            "strength": 0.1,
            "morale": 0.1,
        }
    },
    "player22": {
        "password": generate_password_hash("player22pass"),
        "role": "chaser",
        "skills": {
            "accuracy": 0.1,
            "handling": 0.1,
            "defense": 0.1,
            "agility": 0.1,
            "strength": 0.1,
            "morale": 0.1,
        }
    },
    "player23": {
        "password": generate_password_hash("player23pass"),
        "role": "chaser",
        "skills": {
            "accuracy": 0.1,
            "handling": 0.1,
            "defense": 0.1,
            "agility": 0.1,
            "strength": 0.1,
            "morale": 0.1,
        }
    },
    "player24": {
        "password": generate_password_hash("player24pass"),
        "role": "chaser",
        "skills": {
            "accuracy": 0.1,
            "handling": 0.1,
            "defense": 0.1,
            "agility": 0.1,
            "strength": 0.1,
            "morale": 0.1,
        }
    },
    "player25": {
        "password": generate_password_hash("player25pass"),
        "role": "keeper",
        "skills": {
            "accuracy": 0.1,
            "handling": 0.1,
            "defense": 0.1,
            "agility": 0.1,
            "strength": 0.1,
            "morale": 0.1,
        }
    },
    "player26": {
        "password": generate_password_hash("player26pass"),
        "role": "beater",
        "skills": {
            "accuracy": 0.1,
            "handling": 0.1,
            "defense": 0.1,
            "agility": 0.1,
            "strength": 0.1,
            "morale": 0.1,
        }
    },
    "player27": {
        "password": generate_password_hash("player27pass"),
        "role": "beater",
        "skills": {
            "accuracy": 0.1,
            "handling": 0.1,
            "defense": 0.1,
            "agility": 0.1,
            "strength": 0.1,
            "morale": 0.1,
        }
    },
    "player28": {
        "password": generate_password_hash("player28pass"),
        "role": "seeker",
        "skills": {
            "accuracy": 0.1,
            "handling": 0.1,
            "defense": 0.1,
            "agility": 0.1,
            "strength": 0.1,
            "morale": 0.1,
        }
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
quaffle_possession = None
snitch_caught = False
snitch_spot = False
bludger_approach = []
wounded = []
injured = []
game_started = False
chat_history = []
chat_file = "chat_history.txt"
selected_teams = []
score_chance = 1


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
    <script>
        function updateChat() {
            fetch('/get_chat')
                .then(response => response.json())
                .then(data => {
                    const chatBox = document.getElementById('chat-box');
                    chatBox.innerHTML = data.chat_history.map(msg => `<p>${msg}</p>`).join('');
                    chatBox.scrollTop = chatBox.scrollHeight; // Auto-scroll to the bottom
                })
                .catch(error => console.error('Error updating chat:', error));
        }
        setInterval(updateChat, 2000); // Update every 2 seconds
    </script>
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
    <script>
        function updateChat() {
            fetch('/get_chat')
                .then(response => response.json())
                .then(data => {
                    const chatBox = document.getElementById('chat-box');
                    chatBox.innerHTML = data.chat_history.map(msg => `<p>${msg}</p>`).join('');
                    chatBox.scrollTop = chatBox.scrollHeight; // Auto-scroll to the bottom
                })
                .catch(error => console.error('Error updating chat:', error));
        }
        setInterval(updateChat, 2000); // Update every 2 seconds
    </script>
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
        chat_history.append("The Game has begun and the Chasers rush to get hold of the Quaffle.")
    return redirect(url_for("dashboard"))

@app.route("/end_game", methods=["POST"])
def end_game():
    if "username" in session and session["username"] == "referee":
        global game_started, chat_history, quaffle_possession, snitch_caught, selected_teams
        game_started = False
        chat_history = []
        quaffle_possession = None
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

@app.route("/send_message", methods=["POST"])
def send_message():
    if session["username"] != "referee":
        if "username" not in session or session["username"] not in teams[selected_teams[0]]['players'] + teams[selected_teams[1]]['players']:
            return redirect(url_for("dashboard"))
    
    message = request.form.get("message")
    command = message.split()

    if command[0] == "/":
        if users.get(session['username'])["role"] == 'chaser':
            if command[1] == "Dodge_Player":
                pass
            if command[1] == "Dodge_Bludger":
                pass
            if command[1] == "Namecall":
                pass
            if command[1] == "Pass":
                if session['username'].split()[-1] == quaffle_possession:
                    score_chance *= 1.05
                    chat_history.append(f"{session['username'].split()[-1]} releases a perfect pass, the Quaffle soaring through the air with pinpoint accuracy. {command[-1]} catches it effortlessly, continuing the offensive without missing a beat.")
                    quaffle_possession = command[-1]
            if command[1] == "Shoot":
                pass
            if command[1] == "Dunk":
                pass
            if command[1] == "Snatch":
                if quaffle_possession == None:
                    quaffle_possession = session['username'].split()[-1]
                    chat_history.append(f"{session['username']} has taken possession of the Quaffle.")
            if command[1] == "Wait":
                pass
        if users.get(session['username'])["role"] == 'beater':
            if command[1] == "Namecall":
                pass
            if command[1] == "Defend":
                pass
            if command[1] == "Beat_Bludger":
                pass
            if command[1] == "Double_Hit":
                pass
            if command[1] == "Wait":
                pass
        if users.get(session['username'])["role"] == 'seeker':
            if command[1] == "Seek":
                pass
            if command[1] == "Dodge_Bludger":
                pass
            if command[1] == "Namecall":
                pass
            if command[1] == "Slow_Hover":
                pass
            if command[1] == "Wait":
                pass
        if users.get(session['username'])["role"] == 'keeper':
            if command[1] == "Dodge_Bludger":
                pass
            if command[1] == "Namecall":
                pass
            if command[1] == "Defend":
                pass
            if command[1] == "Block":
                pass
            if command[1] == "Wait":
                pass
            if command[1] == "Slow_Hower":
                pass
            if command[1] == "Pass":
                pass


    chat_history.append(f"{session['username']}: {message}")
    save_chat_history()

    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        return jsonify({"success": True, "message": "Message sent."})

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