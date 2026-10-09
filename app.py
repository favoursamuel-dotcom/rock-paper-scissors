# timer
# Score sheet
import random
from flask import Flask, render_template, request
# import PIL as Image
# import io

app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])

def home():
    choice = None
    computer_choice = None
    result = None
    # paper = None
    # rock = None
    # scissors = None
    
    if request.method == "POST":
        choice = request.form.get("choice")
        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)
        result = winner(choice, computer_choice)
        # paper = request.files["Images/paper.svg"]
        # rock = request.files["Images/rock.svg"]
        # scissors = request.files["Images/scissors.svg"]
    # images = [paper, rock, scissors]
    # for i, image in enumerate(images):
    #     img_byte = image.read()
    #     img = Image.open(io.BytesIO(img_byte))
    #     images[i] = img
    
    return render_template(
        "index.html",
        result=result,
        players_choice=choice,
        computer_choice=computer_choice,
        # paper_img=images[0],
        # rock_img=images[1], 
        # scissors_img=images[2],
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