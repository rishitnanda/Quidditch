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

# HTML template
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Quidditch Game</title>
</head>
<body>
    <h1>Quidditch Multiplayer Game</h1>
    <h2>Team 1 Score: {{ teams['team_1']['score'] }}</h2>
    <h2>Team 2 Score: {{ teams['team_2']['score'] }}</h2>

    {% if snitch_caught %}
    <h3>The game is over! {{ snitch_caught }} wins!</h3>
    {% else %}
    <form action="/play" method="post">
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

        <button type="submit">Join Game</button>
    </form>
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
    return render_template_string(html_template, teams=teams, snitch_caught=snitch_caught)

@app.route("/play", methods=["POST"])
def play():
    global quaffle_possession, snitch_caught

    # Get form data
    player_name = request.form.get("player_name")
    team = request.form.get("team")
    role = request.form.get("role")

    # Add player to team
    if player_name not in teams[team]["players"]:
        teams[team]["players"].append(player_name)

    # Gameplay logic
    if role == "chaser":
        if random.choice([True, False]):
            teams[team]["score"] += 10
            quaffle_possession = team
    elif role == "beater":
        if random.choice([True, False]):
            quaffle_possession = "team_1" if team == "team_2" else "team_2"
    elif role == "keeper":
        if quaffle_possession != team and random.choice([True, False]):
            quaffle_possession = team
    elif role == "seeker":
        if random.randint(1, 100) > 95:  # 5% chance to catch the Snitch
            snitch_caught = team
            teams[team]["score"] += 150

    return render_template_string(html_template, teams=teams, snitch_caught=snitch_caught)

if __name__ == "__main__":
    app.run(debug=True)
