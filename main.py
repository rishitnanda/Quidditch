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
        "team": "team_1",
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
        "team": "team_1",
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
        "team": "team_1",
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
        "team": "team_1",
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
        "team": "team_1",
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
        "team": "team_1",
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
        "team": "team_1",
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
        "team": "team_2",
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
        "team": "team_2",
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
        "team": "team_2",
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
        "team": "team_2",
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
        "team": "team_2",
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
        "team": "team_2",
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
        "team": "team_2",
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
        "team": "team_3",
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
        "team": "team_3",
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
        "team": "team_3",
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
        "team": "team_3",
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
        "team": "team_3",
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
        "team": "team_3",
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
        "team": "team_3",
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
        "team": "team_4",
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
        "team": "team_4",
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
        "team": "team_4",
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
        "team": "team_4",
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
        "team": "team_4",
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
        "team": "team_4",
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
        "team": "team_4",
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

global quaffle_possession, snitch_caught, snitch_spot, wounded, injured, game_started, chat_history, chat_file, selected_teams, score_chance, snatch_event, snatching, dodge
quaffle_possession = None
snitch_caught = False
snitch_spot = False
wounded = []
injured = []
game_started = False
chat_history = []
chat_file = "chat_history.txt"
selected_teams = []
score_chance = 1
snatch_event = False
snatching = []
dodge = []


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
    global quaffle_possession, snitch_caught, snitch_spot, bludger_approach, wounded, injured, game_started, chat_history, chat_file, selected_teams, score_chance, snatch_event, snatching, dodge
    if session["username"] != "referee":
        if "username" not in session or session["username"] not in teams[selected_teams[0]]['players'] + teams[selected_teams[1]]['players']:
            return redirect(url_for("dashboard"))
    print(quaffle_possession)
    message = request.form.get("message")
    command = message.split()

    if command[0][0] == "/" and snitch_caught == False:
        if users.get(session['username'])["role"] == 'chaser':
            try:
                if snatching[1] == session['username']:
                    if command[0][1:] == "Dodge_Player":
                        if random.uniform(0,100)/100 < ((users.get(session['username'])["skills"]["handling"]) + (users.get(session['username'])["skills"]["defense"]) + (users.get(session['username'])["skills"]["agility"]))/3:
                            chat_history.append(f"With a swift sidestep, {session['username']} skillfully evades {snatching[0]}’s pursuit, gracefully maintaining control of the Quaffle. Their handling proves exceptional as they regain their momentum.")
                        else:
                            chat_history.append(f"{session['username']} attempts to dodge but fails to shake off {snatching[0]}, their movements too predictable. {snatching[0]} closes in, forcing {session['username']} to lose possession of the Quaffle.")
                            quaffle_possession = snatching[0]
                            score_chance = 1
                            users.get(session['username'])["skills"]["handling"] *= 0.9
                        snatch_event = False
                        snatching = []
            except:
                pass

            if session['username'] in dodge:
                if command[0][1:] == "Dodge_Bludger":
                    if random.uniform(0,100)/100 < ((users.get(session['username'])["skills"]["agility"]) + (users.get(session['username'])["skills"]["defense"]) + (users.get(session['username'])["skills"]["handling"]))/3:
                        chat_history.append(f"{session['username']} ducks at the last second, narrowly avoiding the incoming bludger. They remain unscathed and maintain possession, their agility and quick thinking preventing any setback.")
                    else:
                        chat_history.append(f"A well-timed bludger strikes {session['username']} squarely, knocking them off course. Their handling falters as they struggle to regain their footing.")
                        users.get(session['username'])["skills"]["agility"] *= 0.9
                        users.get(session['username'])["skills"]["handling"] *= 0.9
                        if quaffle_possession == session['username']:
                            quaffle_possession = None
                            chat_history.append(f"{session['username']} loses possession of the Quaffle which is now up for grabs.")
                        
                        t = random.random()
                        if t < 0.08:
                            chat_history.append(f"{session['username']} is wounded and moves away from the field.")
                            wounded.append(session['username'])
                        elif 0.08 < t < 0.11:
                            chat_history.append(f"{session['username']} is injured and leaves for a while to be treated.")
                            injured.append(session['username'])

                    dodge.remove(session['username'])

            else:
                if command[0][1:] == "Namecall" and session['username'] not in wounded and session['username'] not in injured:
                    if users.get(session['username'])['team'] != users.get(command[-1])['team']:
                        if random.uniform(0,100)/100 < abs((users.get(session['username'])["skills"]["morale"]) - (users.get(session['username'])["skills"]["strength"]))/2:
                            (users.get(command[-1])["skills"]["morale"]) *= 0.95
                            if random.uniform(0,100)/100 < 0.2:
                                chat_history.append(f"{session['username']} delivers a biting taunt to {command[-1]}, throwing them off their game who hesitates, visibly shaken by the remark. A warning is issued for unsportsmanlike conduct to {session['username']}.")
                            else:
                                chat_history.append(f"{command[-1]} looks fazed, wonder what happened.")
                        else:
                            if random.uniform(0,100)/100 < 0.2:
                                chat_history.append(f"{session['username']} delivers a biting taunt to {command[-1]}, who remains unfazed. A warning is issued for unsportsmanlike conduct to {session['username']}.")
                            else:
                                chat_history.append(f"{command[-1]} swoops past {session['username']}.")

                elif command[0][1:] == "Pass" and session['username'] not in wounded and session['username'] not in injured:
                    if session['username'] == quaffle_possession and users.get(session['username'])['team'] == users.get(command[-1])['team']:
                        score_chance *= 1.05
                        chat_history.append(f"{session['username']} releases a perfect pass, the Quaffle soaring through the air with pinpoint accuracy. {command[-1]} catches it effortlessly, continuing the offensive without missing a beat.")
                        quaffle_possession = command[-1]

                elif command[0][1:] == "Shoot" and session['username'] not in wounded and session['username'] not in injured:
                    if session['username'] == quaffle_possession:
                        if random.uniform(0,100)/100 < score_chance * ((users.get(session['username'])["skills"]["accuracy"] * 0.4) + (users.get(session['username'])["skills"]["handling"] * 0.3) + (users.get(session['username'])["skills"]["strength"] * 0.2) + (users.get(session['username'])["skills"]["agility"] * 0.1) + (users.get(session['username'])["skills"]["morale"] * 0.05)):
                            chat_history.append(f"{session['username']} lines up and fires a calculated shot. The Quaffle arcs gracefully through the air, a flawless display of precision and strength.")
                            users.get(session['username'])["skills"]["strength"] * 0.97
                            quaffle_possession = "Goal" + users.get(session['username'])['team'][-4]

                elif command[0][1:] == "Dunk" and session['username'] not in wounded and session['username'] not in injured:
                    if session['username'] == quaffle_possession:
                        if random.uniform(0,100)/100 < score_chance * ((users.get(session['username'])["skills"]["accuracy"] * 0.1) + (users.get(session['username'])["skills"]["handling"] * 0.05) + (users.get(session['username'])["skills"]["strength"] * 0.1) + (users.get(session['username'])["skills"]["agility"] * 0.1) + (users.get(session['username'])["skills"]["morale"] * 0.1)):
                            chat_history.append(f"In a stunning display of athleticism, {session['username']} leaps towards the hoop, executing a perfect dunk that leaves the crowd roaring. Their timing and power were immaculate, making the keeper's block impossible who now has the quaffle.")
                        else:
                            chat_history.append(f"{session['username']} attempts a dunk but is blocked by the keeper who now has the quaffle.")
                        users.get(session['username'])["skills"]["strength"] * 0.93
                        users.get(session['username'])["skills"]["defense"] * 0.93
                        quaffle_possession = users.get(session['username'])['team'][-4]

                elif command[0][1:] == "Snatch" and session['username'] not in wounded and session['username'] not in injured:
                    if quaffle_possession == None:
                        quaffle_possession = session['username']
                        chat_history.append(f"{session['username']} has taken possession of the Quaffle.")
                    else:
                        if snatch_event == False and quaffle_possession != session['username'] and quaffle_possession == command[-1] and users.get(session['username'])['team'] != users.get(command[-1])['team']:
                            snatch_event = True
                            chat_history.append(f"{session['username']} approaches {quaffle_possession} from behind in an attempt to claim the ball.")
                            snatching.append(session['username'])
                            snatching.append(quaffle_possession)

                elif command[0][1:] == "Wait":
                    users.get(session['username'])["skills"][random.choice(list(users.get(session['username'])["skills"].keys()))] *= 1.02

        if users.get(session['username'])["role"] == 'beater':
            if command[0][1:] == "Namecall" and session['username'] not in dodge and session['username'] not in wounded and session['username'] not in injured:
                if users.get(session['username'])['team'] != users.get(command[-1])['team']:
                    if random.uniform(0,100)/100 < abs((users.get(session['username'])["skills"]["morale"]) - (users.get(session['username'])["skills"]["strength"]))/2:
                        (users.get(command[-1])["skills"]["morale"]) *= 0.95
                        if random.uniform(0,100)/100 < 0.2:
                            chat_history.append(f"{session['username']} delivers a biting taunt to {command[-1]}, throwing them off their game who hesitates, visibly shaken by the remark. A warning is issued for unsportsmanlike conduct to {session['username']}.")
                        else:
                            chat_history.append(f"{command[-1]} looks fazed, wonder what happened.")
                    else:
                        if random.uniform(0,100)/100 < 0.2:
                            chat_history.append(f"{session['username']} delivers a biting taunt to {command[-1]}, who remains unfazed. A warning is issued for unsportsmanlike conduct to {session['username']}.")
                        else:
                            chat_history.append(f"{command[-1]} swoops past {session['username']}.")

            elif command[0][1:] == "Defend" and session['username'] not in dodge and session['username'] not in wounded and session['username'] not in injured:
                if random.uniform(0,100)/100 < abs((users.get(session['username'])["skills"]["strength"]) + (users.get(session['username'])["skills"]["morale"]))/2:
                    chat_history.append(f"{session['username']} steps in front of {command[-1]} with impeccable timing, using their strength to block an incoming bludger. Their defensive play keeps the team safe and the offense in motion.")
                else:
                    chat_history.append(f"A well-timed bludger strikes {command[-1]} squarely, knocking them off course. Their handling falters as they struggle to regain their footing.")
                    users.get(session['username'])["skills"]["strength"] *= 0.9
                    users.get(session['username'])["skills"]["defense"] *= 0.9
                dodge.remove(command[-1])

            elif command[0][1:] == "Beat_Bludger" and session['username'] not in wounded and session['username'] not in injured and command[-1] not in dodge and command[-1] not in wounded and command[-1] not in injured:
                if random.uniform(0,100)/100 < abs((users.get(session['username'])["skills"]["accuracy"]) + (users.get(session['username'])["skills"]["handling"]))/2:
                    chat_history.append(f"With a powerful swing, {session['username']} sends a bludger flying directly towards {command[-1]}.")
                    dodge.append(command[-1])
                    if session['username'] in dodge:
                        dodge.remove(session['username'])
                else:
                    chat_history.append(f"{session['username']} misses their target, the bludger sailing off course. Their aim is off, and the opposing player continues without hindrance, maintaining their offensive drive unhindered.")
                    if session['username'] in dodge:
                        dodge.remove(session['username'])
                        users.get(session['username'])["skills"]["agility"] *= 0.9
                        users.get(session['username'])["skills"]["handling"] *= 0.9
                        
                        t = random.random()
                        if t < 0.08:
                            chat_history.append(f"{session['username']} is wounded and moves away from the field.")
                            wounded.append(session['username'])
                        elif 0.08 < t < 0.11:
                            chat_history.append(f"{session['username']} is injured and leaves for a while to be treated.")
                            injured.append(session['username'])


            elif command[0][1:] == "Double_Hit" and session['username'] not in dodge and session['username'] not in wounded and session['username'] not in injured and command[-1] not in dodge and command[-1] not in wounded and command[-1] not in injured:
                if random.uniform(0,100)/100 < abs((users.get(session['username'])["skills"]["agility"]) + (users.get(session['username'])["skills"]["defense"]))/2:
                    chat_history.append(f"With a powerful swing, {session['username']} sends bludgers flying directly towards {command[-1]}.")
                    dodge.append(command[-1])
                else:
                    chat_history.append(f"{session['username']} misses their target, the bludgers sailing off course. Their aim is off, and the opposing player continues without hindrance, maintaining their offensive drive unhindered.")

            elif command[0][1:] == "Wait" and session['username'] not in dodge:
                users.get(session['username'])["skills"][random.choice(list(users.get(session['username'])["skills"].keys()))] *= 1.02

        if users.get(session['username'])["role"] == 'seeker':
            if session['username'] in dodge:
                if command[0][1:] == "Dodge_Bludger":
                    if random.uniform(0,100)/100 < ((users.get(session['username'])["skills"]["agility"]) + (users.get(session['username'])["skills"]["defense"]) + (users.get(session['username'])["skills"]["handling"]))/3:
                        chat_history.append(f"{session['username']} ducks at the last second, narrowly avoiding the incoming bludger. They remain unscathed and maintain possession, their agility and quick thinking preventing any setback.")
                    else:
                        chat_history.append(f"A well-timed bludger strikes {session['username']} squarely, knocking them off course. Their handling falters as they struggle to regain their footing.")
                        users.get(session['username'])["skills"]["agility"] *= 0.9
                        users.get(session['username'])["skills"]["handling"] *= 0.9
                        
                        t = random.random()
                        if t < 0.08:
                            chat_history.append(f"{session['username']} is wounded and moves away from the field.")
                            wounded.append(session['username'])
                        elif 0.08 < t < 0.11:
                            chat_history.append(f"{session['username']} is injured and leaves for a while to be treated.")
                            injured.append(session['username'])

                    dodge.remove(session['username'])
            
            else:
                if command[0][1:] == "Dive" and snitch_spot == True and session['username'] not in wounded and session['username'] not in injured:
                    if random.uniform(0,100)/100 < ((users.get(session['username'])["skills"]["agility"]) * 0.1) + ((users.get(session['username'])["skills"]["accuracy"]) * 0.1):
                        users.get(session['username'])['team']["score"] += 150
                        score1 = teams.get(selected_teams[0])["score"]
                        score2 = teams.get(selected_teams[1])["score"]
                        winner = selected_teams[0] if score1 > score2 else selected_teams[1]
                        chat_history.append(f"{session['username']} plunges forward with impressive speed and has caught the snitch. Game Over! {winner} wins by {score1} — {score2}.")
                        snitch_caught = True
                    else:
                        chat_history.append(f"{session['username']} dives for the snitch but misses it.")
                        if random.uniform(0,100)/100 < 0.1:
                            snitch_spot = False

                elif command[0][1:] == "Namecall" and session['username'] not in wounded and session['username'] not in injured:
                    if users.get(session['username'])['team'] != users.get(command[-1])['team']:
                        if random.uniform(0,100)/100 < abs((users.get(session['username'])["skills"]["morale"]) - (users.get(session['username'])["skills"]["strength"]))/2:
                            (users.get(command[-1])["skills"]["morale"]) *= 0.95
                            if random.uniform(0,100)/100 < 0.2:
                                chat_history.append(f"{session['username']} delivers a biting taunt to {command[-1]}, throwing them off their game who hesitates, visibly shaken by the remark. A warning is issued for unsportsmanlike conduct to {session['username']}.")
                            else:
                                chat_history.append(f"{command[-1]} looks fazed, wonder what happened.")
                        else:
                            if random.uniform(0,100)/100 < 0.2:
                                chat_history.append(f"{session['username']} delivers a biting taunt to {command[-1]}, who remains unfazed. A warning is issued for unsportsmanlike conduct to {session['username']}.")
                            else:
                                chat_history.append(f"{command[-1]} swoops past {session['username']}.")
                                
                elif command[0][1:] == "Slow_Hover" and session['username'] not in wounded and session['username'] not in injured:

                    if random.uniform(0,100)/100 < ((users.get(session['username'])["skills"]["agility"]) * 0.5) + ((users.get(session['username'])["skills"]["handling"]) * 0.5):
                        chat_history.append(f"{session['username']} hovers gracefully over the pitch. Wait, is that the snitch?")
                        snitch_spot = True
                    else:
                        chat_history.append(f"{session['username']}’s slow hover drags on, leaving them vulnerable.")
                    
                    if random.uniform(0,100)/100 < ((users.get(session['username'])["skills"]["agility"]) * 0.1) + ((users.get(session['username'])["skills"]["accuracy"]) * 0.1):
                        users.get(session['username'])['team']["score"] += 150
                        score1 = teams.get(selected_teams[0])["score"]
                        score2 = teams.get(selected_teams[1])["score"]
                        winner = selected_teams[0] if score1 > score2 else selected_teams[1]
                        chat_history.append(f"{session['username']} plunges forward with impressive speed and has caught the snitch. Game Over! {winner} wins by {score1} — {score2}.")
                        snitch_caught = True
                    else:
                        chat_history.append(f"{session['username']} dives for the snitch but misses it.")
                        if random.uniform(0,100)/100 < 0.1:
                            snitch_spot = False

                elif command[0][1:] == "Wait":
                    users.get(session['username'])["skills"][random.choice(list(users.get(session['username'])["skills"].keys()))] *= 1.02

        if users.get(session['username'])["role"] == 'keeper':
            if session['username'] in dodge:
                if command[0][1:] == "Dodge_Bludger":
                    if random.uniform(0,100)/100 < ((users.get(session['username'])["skills"]["agility"]) + (users.get(session['username'])["skills"]["defense"]) + (users.get(session['username'])["skills"]["handling"]))/3:
                        chat_history.append(f"{session['username']} ducks at the last second, narrowly avoiding the incoming bludger. They remain unscathed and maintain possession, their agility and quick thinking preventing any setback.")
                    else:
                        chat_history.append(f"A well-timed bludger strikes {session['username']} squarely, knocking them off course. Their handling falters as they struggle to regain their footing.")
                        users.get(session['username'])["skills"]["agility"] *= 0.9
                        users.get(session['username'])["skills"]["handling"] *= 0.9
                        
                        t = random.random()
                        if t < 0.08:
                            chat_history.append(f"{session['username']} is wounded and moves away from the field.")
                            wounded.append(session['username'])
                        elif 0.08 < t < 0.11:
                            chat_history.append(f"{session['username']} is injured and leaves for a while to be treated.")
                            injured.append(session['username'])

                        if quaffle_possession == session['username']:
                            quaffle_possession = None
                            chat_history.append(f"{session['username']} loses possession of the Quaffle which is now up for grabs.")
                    dodge.remove(session['username'])

            elif quaffle_possession == session['username']:
                if command[0][1:] == "Pass":
                    if users.get(session['username'])['team'] == users.get(command[-1])['team']:
                        chat_history.append(f"{session['username']} releases a perfect pass, the Quaffle soaring through the air with pinpoint accuracy. {command[-1]} catches it effortlessly, continuing the offensive without missing a beat.")
                        quaffle_possession = command[-1]

            else:
                if command[0][1:] == "Namecall":
                    if users.get(session['username'])['team'] != users.get(command[-1])['team']:
                        if random.uniform(0,100)/100 < abs((users.get(session['username'])["skills"]["morale"]) - (users.get(session['username'])["skills"]["strength"]))/2:
                            (users.get(command[-1])["skills"]["morale"]) *= 0.95
                            if random.uniform(0,100)/100 < 0.2:
                                chat_history.append(f"{session['username']} delivers a biting taunt to {command[-1]}, throwing them off their game who hesitates, visibly shaken by the remark. A warning is issued for unsportsmanlike conduct to {session['username']}.")
                            else:
                                chat_history.append(f"{command[-1]} looks fazed, wonder what happened.")
                        else:
                            if random.uniform(0,100)/100 < 0.2:
                                chat_history.append(f"{session['username']} delivers a biting taunt to {command[-1]}, who remains unfazed. A warning is issued for unsportsmanlike conduct to {session['username']}.")
                            else:
                                chat_history.append(f"{command[-1]} swoops past {session['username']}.")
                                
                elif command[0][1:] == "Defend":
                    if random.uniform(0,100)/100 < ((users.get(session['username'])["skills"]["agility"]) * 0.5) + ((users.get(session['username'])["skills"]["morale"]) * 0.5):
                        for i in users.get(session['username'])['team']['players']:
                            users.get(i)["skills"]["defense"] *= 1.05
                        chat_history.append(f"{session['username']} braces themselves, their defense bolstered by a surge of determination.")

                elif command[0][1:] == "Block" and quaffle_possession == "Goal" + session['username']:
                    if random.uniform(0,100)/100 < ((users.get(session['username'])["skills"]["strength"]) + (users.get(session['username'])["skills"]["morale"]) + (users.get(session['username'])["skills"]["defense"]))/3:
                        chat_history.append(f"{session['username']} leaps into action, blocking the incoming Quaffle with a powerful save. Their strength and reflexes were unmatched, preventing a goal.")
                    else:
                        chat_history.append(f"{session['username']} attempts to block the Quaffle but fails to stop the goal.")
                        r = selected_teams[0] if selected_teams[0] != teams.get(users.get(session['username'])['team']) else selected_teams[1]
                        s = selected_teams[0] if selected_teams[0] == teams.get(users.get(session['username'])['team']) else selected_teams[1]
                        users.get(session['username'])['team']["score"] += 10
                        chat_history.append(f"Goal! 10 points to {s}.")
                        score_chance = 1
                    quaffle_possession = session['username']

                elif command[0][1:] == "Slow_Hower":
                    chat_history.append(f"{session['username']} hovers in front of the goal hoops watching the quaffle carefully.")
                    users.get(session['username'])["skills"]["defense"] *= 1.1
                    users.get(session['username'])["skills"]["strength"] *= 1.1
                    users.get(session['username'])["skills"]["agility"] *= 0.9

                elif command[0][1:] == "Wait":
                    users.get(session['username'])["skills"][random.choice(list(users.get(session['username'])["skills"].keys()))] *= 1.02
    else:
        chat_history.append(f"{session['username']}: {message}")

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