import random

# Rules of the game

def check_winner(player, computer):
    if (player == computer):
        return "It's a tie!!"
    elif (player == "rock" and computer == "scissors") or \
            (player == "scissors" and computer == "paper") or \
            (player == "paper" and computer == "rock"):
        return "You Win!!"
    else:
        return "Computer Wins!!"
    
# Options for the game

options = ["rock", "paper", "scissors"]

# Start the game


print("Welcome to the Rock, Paper and Scissors Game")
player_choice = input("Enter your choice (rock/paper/scissors): ").lower()

if player_choice not in options:
    print("Invalid choice. Please choose rock, paper or scissors!")
else:
    computer_choice = random.choice(options)
    print(f"Computer chose: {computer_choice} ")
    print(check_winner(player_choice, computer_choice))