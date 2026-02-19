from flask import Flask, render_template_string, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = "supersecretkey"

def new_game():
    session['player_hp'] = 100
    session['enemy_hp'] = random.randint(50, 100)
    session['message'] = "A wild monster appears! 👹"

@app.route('/')
def home():
    if 'player_hp' not in session:
        new_game()

    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Mini Flask RPG</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #1e1e2f;
                color: white;
                text-align: center;
                padding: 40px;
            }
            .card {
                background: #2c2c3c;
                padding: 30px;
                border-radius: 15px;
                max-width: 500px;
                margin: auto;
                box-shadow: 0 0 20px rgba(0,0,0,0.5);
            }
            button {
                padding: 10px 20px;
                margin: 10px;
                font-size: 16px;
                border: none;
                border-radius: 8px;
                cursor: pointer;
            }
            .attack { background-color: crimson; color: white; }
            .heal { background-color: seagreen; color: white; }
            .restart { background-color: gray; color: white; }
            h1 { margin-bottom: 10px; }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>⚔️ Mini RPG Battle ⚔️</h1>
            <p><strong>Your HP:</strong> {{ player_hp }}</p>
            <p><strong>Enemy HP:</strong> {{ enemy_hp }}</p>
            <p>{{ message }}</p>

            {% if player_hp > 0 and enemy_hp > 0 %}
                <a href="/attack"><button class="attack">Attack 🗡️</button></a>
                <a href="/heal"><button class="heal">Heal ❤️</button></a>
            {% else %}
                <a href="/restart"><button class="restart">Restart Game 🔄</button></a>
            {% endif %}
        </div>
    </body>
    </html>
    """

    return render_template_string(
        html,
        player_hp=session['player_hp'],
        enemy_hp=session['enemy_hp'],
        message=session['message']
    )

@app.route('/attack')
def attack():
    player_damage = random.randint(10, 25)
    enemy_damage = random.randint(5, 20)

    session['enemy_hp'] -= player_damage
    session['player_hp'] -= enemy_damage

    if session['enemy_hp'] <= 0:
        session['message'] = f"You dealt {player_damage} damage and defeated the monster! 🎉"
    elif session['player_hp'] <= 0:
        session['message'] = f"You dealt {player_damage} damage, but the monster defeated you... 💀"
    else:
        session['message'] = f"You dealt {player_damage} damage. The monster hit back for {enemy_damage}!"

    return redirect(url_for('home'))

@app.route('/heal')
def heal():
    heal_amount = random.randint(10, 20)
    enemy_damage = random.randint(5, 15)

    session['player_hp'] += heal_amount
    session['player_hp'] -= enemy_damage

    session['message'] = f"You healed for {heal_amount}, but the monster attacked for {enemy_damage}!"

    return redirect(url_for('home'))

@app.route('/restart')
def restart():
    new_game()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
