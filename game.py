
import random


def game():

    attempt = 0

    player_score = 0
    computer_score = 0

    choices = ["rock", "paper", "scissors"]

    while True:

        print("The player and computer can choose:")
        print("1. Rock  2. Paper  3. Scissors")
        print("Best of five attempts wins")

        players_choice = input(
            "Please choose one from the choices above: "
        ).lower()

        # Quit the game
        if players_choice == "q":
            print("Thanks for playing!")
            break

        # Validate the player's choice
        if players_choice not in choices:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        # Only count valid attempts
        attempt += 1

        computer_choice = random.choice(choices)

        print(f"\nYou chose: {players_choice}")
        print(f"Computer chose: {computer_choice}")

        if players_choice == computer_choice:

            print("It is a draw!")

        elif players_choice == "rock" and computer_choice == "paper":

            print("Paper covers Rock")
            print("You lost!")
            computer_score += 1

        elif players_choice == "rock" and computer_choice == "scissors":

            print("Rock breaks Scissors")
            print("You won!")
            player_score += 1

        elif players_choice == "paper" and computer_choice == "rock":

            print("Paper covers Rock")
            print("You won!")
            player_score += 1

        elif players_choice == "paper" and computer_choice == "scissors":

            print("Scissors cut Paper")
            print("You lost!")
            computer_score += 1

        elif players_choice == "scissors" and computer_choice == "rock":

            print("Rock breaks Scissors")
            print("You lost!")
            computer_score += 1

        elif players_choice == "scissors" and computer_choice == "paper":

            print("Scissors cut Paper")
            print("You won!")
            player_score += 1

        print(f"Score: You {player_score} - Computer {computer_score}")

        # End the game after five valid attempts
        if attempt == 5:
            print("\n===== GAME OVER =====")

            if player_score > computer_score:
                print("Congratulations! You won the game!")

            elif computer_score > player_score:
                print("The computer won the game. Better luck next time!")

            else:
                print("The game ended in a draw!")

            print(f"Final score: You {player_score} - Computer {computer_score}")
            break


game()