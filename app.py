from flask import Flask, render_template_string
import random
from datetime import datetime

app = Flask(__name__)

fun_facts = [
    "Python was named after Monty Python 🐍",
    "Flask is called a microframework, but it's powerful!",
    "VS Code is one of the most popular code editors 🚀",
    "The first computer bug was an actual moth 🦋",
    "You can build APIs, websites, and more with Flask!"
]

@app.route('/')
def home():
    fact = random.choice(fun_facts)
    current_time = datetime.now().strftime("%A, %B %d, %Y %I:%M %p")

    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>My Pretty Flask App</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #667eea, #764ba2);
                color: white;
                text-align: center;
                padding: 50px;
            }
            .card {
                background: rgba(255, 255, 255, 0.15);
                padding: 40px;
                border-radius: 15px;
                backdrop-filter: blur(10px);
                box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
                max-width: 600px;
                margin: auto;
            }
            h1 {
                font-size: 2.5em;
                margin-bottom: 10px;
            }
            .time {
                font-size: 1.1em;
                margin-bottom: 20px;
                opacity: 0.9;
            }
            .fact {
                margin-top: 20px;
                font-size: 1.2em;
                font-style: italic;
            }
            button {
                margin-top: 25px;
                padding: 10px 20px;
                font-size: 1em;
                border: none;
                border-radius: 8px;
                background-color: #ffffff;
                color: #764ba2;
                cursor: pointer;
                transition: 0.3s;
            }
            button:hover {
                background-color: #f1f1f1;
                transform: scale(1.05);
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>✨ Welcome to My Flask App ✨</h1>
            <div class="time">Current time: {{ time }}</div>
            <p>This app is running beautifully in VS Code 🎉</p>
            <div class="fact">Fun Fact: {{ fact }}</div>
            <button onclick="window.location.reload();">Show Another Fun Fact</button>
        </div>
    </body>
    </html>
    """

    return render_template_string(html, fact=fact, time=current_time)

if __name__ == '__main__':
    app.run(debug=True)
