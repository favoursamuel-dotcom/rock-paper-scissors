# 1. Get the player's choice          ↓# 2. Generate the computer's choice
# 3. Compare the two choice             # 4. Determine the winner   # 5. Display the result

import random
def Game():
    print("The player and computer can choose:  1. Rock"  "2. Paper"  "3. Scissors")
    choices = ["rock", "paper", "scissors"]
    Players_choice = input("Please choose one from the choices above: ")
    computer_choice = random.choice(choices)
    if Players_choice == computer_choice:
        print("Draw, Try again !!")
    elif Players_choice == "rock" and computer_choice == "paper":
        print("Paper covers Rock")
        print("You lost! Try again")
    elif Players_choice == "rock" and computer_choice == "scissors":
        print("Rock breaks Scissors.")
        print("You Won !!")
    elif Players_choice == "paper" and computer_choice == "rock":
        print("Paper covers Rock.")
        print("You Won!!")
    elif Players_choice == "paper" and computer_choice == "scissors":
        print("Scissors cut Paper")
        print("You lost! Try again")
    elif Players_choice == "scissors" and computer_choice == "rock":
        print("Rock breaks Scissors")
        print("You lost! Try again")
    else:
        print("Scissors cuts Paper")
        print("You Won!!")
Game()