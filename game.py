# 1. Get the player's choice          ↓# 2. Generate the computer's choice
# 3. Compare the two choice             # 4. Determine the winner   # 5. Display the result

import random
def game():
    attempt = 0
    sum = 0
    while True:
        print("The player and computer can choose:  1. Rock"  " 2. Paper"  " 3. Scissors" "4. Q")
        print("Best of five attempt wins")
        choices = ["rock", "paper", "scissors"]
        players_choice = input("Please choose one from the choices above: ").lower()
        computer_choice = random.choice(choices)
        attempt +=1
        if players_choice not in choices:
            print("Invalid choice")
            continue
        if players_choice == computer_choice:
            print("It is a draw !!")
        elif players_choice == "rock" and computer_choice == "paper":
            print("Paper covers Rock")
            print("You lost! Try again")
        elif players_choice == "rock" and computer_choice == "scissors":
            print("Rock breaks Scissors.")
            print("You Won !!")
        elif players_choice == "paper" and computer_choice == "rock":
            print("Paper covers Rock.")
            print("You Won!!")
        elif players_choice == "paper" and computer_choice == "scissors":
            print("Scissors cut Paper")
            print("You lost! Try again")
        elif players_choice == "scissors" and computer_choice == "rock":
            print("Rock breaks Scissors")
            print("You lost! Try again")
        elif players_choice == "scissors" and computer_choice == "paper":
            print("Scissors cuts Paper")
            print("You Won!!")
        else:
            print("Invalid input: choose between rock, paper or scissors")
       if attempt > 5:
game()