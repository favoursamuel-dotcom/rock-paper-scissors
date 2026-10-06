import random
from flask import Flask, render_template, request

app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])

def home():
    choice = request.form.get("choice")
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    result = winner(choice, computer_choice)
    return render_template("index.html",
        result=result,
        player_choice=choice,
        computer_choice=computer_choice
    )

def winner(players_choice, computer_choice):

    if players_choice == computer_choice:
        return "It is a draw"

    elif players_choice == "rock" and computer_choice == "paper":
        return "Paper covers Rock — You lost!"

    elif players_choice == "rock" and computer_choice == "scissors":
        return "Rock breaks Scissors — You won!"

    elif players_choice == "paper" and computer_choice == "rock":
        return "Paper covers Rock — You won!"

    elif players_choice == "paper" and computer_choice == "scissors":
        return "Scissors cut Paper — You lost!"

    elif players_choice == "scissors" and computer_choice == "rock":
        return "Rock breaks Scissors — You lost!"

    elif players_choice == "scissors" and computer_choice == "paper":
        return "Scissors cut Paper — You won!"

if __name__ == "__main__":
    app.run(debug=True)