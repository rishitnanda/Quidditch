from flask import Flask, request, jsonify, render_template_string
import random

app = Flask(__name__)

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

# HTML template
html_template = """
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
    <form action="/join" method="post">
        <h3>Join the Game</h3>
        <label for="player_name">Player Name:</label>
        <input type="text" id="player_name" name="player_name" required><br><br>

        <label for="team">Choose Team:</label>
        <select id="team" name="team">
            <option value="team_1">Team 1</option>
            <option value="team_2">Team 2</option>
        </select><br><br>

        <label for="role">Choose Role:</label>
        <select id="role" name="role">
            <option value="chaser">Chaser</option>
            <option value="beater">Beater</option>
            <option value="keeper">Keeper</option>
            <option value="seeker">Seeker</option>
        </select><br><br>

        <button type="submit" class="action-button">Join Game</button>
    </form>
    
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
</body>
</html>
"""

@app.route("/", methods=["GET"])
def index():
    return render_template_string(html_template, teams=teams, snitch_caught=snitch_caught, current_event=current_event)

@app.route("/join", methods=["POST"])
def join():
    player_name = request.form.get("player_name")
    team = request.form.get("team")
    role = request.form.get("role")

    if player_name not in teams[team]["players"]:
        teams[team]["players"].append({"name": player_name, "role": role})

    return render_template_string(html_template, teams=teams, snitch_caught=snitch_caught, current_event=current_event)

@app.route("/action", methods=["POST"])
def action():
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
    
    return render_template_string(html_template, teams=teams, snitch_caught=snitch_caught, current_event=current_event)

if __name__ == "__main__":
    app.run(debug=True)
