import random

# Rules of the game

def check_winner(player, computer):
    if (player == computer):
        return "It's a tie!!"
    elif (player == "snake" and computer == "water") or \
            (player == "water" and computer == "gun") or \
            (player == "gun" and computer == "snake"):
        return "You Win!!"
    else:
        return "Computer Wins!!"
    
# Options for the game

options = ["snake", "water", "gun"]

# Start the game


print("Welcome to the Snake, Water and Gun Game")
player_choice = input("Enter your choice (snake/water/gun): ").lower()

if player_choice not in options:
    print("Invalid choice. Please choose snake, water or gun!")
else:
    computer_choice = random.choice(options)
    print(f"Computer chose: {computer_choice} ")
    print(check_winner(player_choice, computer_choice))