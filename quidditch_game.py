from flask import Flask, request, jsonify, render_template_string, session, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash

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
        "role": "player"
    },
    "player2": {
        "password": generate_password_hash("player2pass"),
        "role": "player"
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
    {% if error %}
    <p style="color: red;">{{ error }}</p>
    {% endif %}
</body>
</html>
"""

game_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Quidditch Game</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        .options { margin: 10px 0; }
        .action-button { margin: 5px; padding: 10px 15px; font-size: 16px; cursor: pointer; }
    </style>
</head>
<body>
    <h1>Quidditch Multiplayer Game</h1>
    <h2>Team 1 Score: {{ teams['team_1']['score'] }}</h2>
    <h2>Team 2 Score: {{ teams['team_2']['score'] }}</h2>

    {% if snitch_caught %}
    <h3>The game is over! {{ snitch_caught }} wins!</h3>
    {% else %}
    <h3>Current Event: {{ current_event }}</h3>
    <div class="options">
        <form action="/action" method="post">
            <button name="action" value="catch_quaffle" class="action-button">Catch Quaffle</button>
            <button name="action" value="snatch_snitch" class="action-button">Snatch Snitch</button>
            <button name="action" value="dodge" class="action-button">Dodge</button>
            <button name="action" value="hit_bludger" class="action-button">Hit with Bludger</button>
            <button name="action" value="name_calling" class="action-button">Name Calling</button>
        </form>
    </div>
    {% endif %}

    <h3>Players:</h3>
    <ul>
        <li>Team 1: {{ teams['team_1']['players'] }}</li>
        <li>Team 2: {{ teams['team_2']['players'] }}</li>
    </ul>
    <form action="/logout" method="post">
        <button type="submit">Logout</button>
    </form>
</body>
</html>
"""

@app.route("/", methods=["GET"])
def index():
    if "username" not in session:
        return redirect(url_for("login"))
    return render_template_string(game_template, teams=teams, snitch_caught=snitch_caught, current_event=current_event)

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

@app.route("/action", methods=["POST"])
def action():
    if "username" not in session:
        return redirect(url_for("login"))

    global quaffle_possession, snitch_caught, current_event
    action = request.form.get("action")
    event_outcomes = {
        "catch_quaffle": "Chaser catches the Quaffle!",
        "snatch_snitch": "Seeker dives for the Snitch!",
        "dodge": "Player dodges expertly!",
        "hit_bludger": "Beater hits the Bludger!",
        "name_calling": "A player uses distracting name-calling!"
    }

    if action in event_outcomes:
        current_event = event_outcomes[action]
        if action == "catch_quaffle":
            teams[quaffle_possession]["score"] += 10
        elif action == "snatch_snitch":
            if random.randint(1, 100) > 80:  # 20% chance to catch the Snitch
                snitch_caught = quaffle_possession
                teams[quaffle_possession]["score"] += 150

    return render_template_string(game_template, teams=teams, snitch_caught=snitch_caught, current_event=current_event)

if __name__ == "__main__":
    app.run(debug=True)
