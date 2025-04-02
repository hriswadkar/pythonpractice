import random as r

number = r.randint(1, 100)

print("Computer has generated a random number between 1 and 100. Take a guess!!! ")
guess = -1
noOfGuesses = 1

while(guess != number):    
    guess = int(input("Please enter correct guess: "))
    if (guess > number):
        print("Lower number please")
        noOfGuesses += 1
    elif (guess < number):
        print("Higher number please")
        noOfGuesses += 1
    else:
        print("Correct guess")
    

print(f"Number of guesses {noOfGuesses}")