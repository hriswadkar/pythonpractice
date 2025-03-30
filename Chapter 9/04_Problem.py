# A file contains word "Donkey". Write a program that replaces the word donkey with ###### and update it in the file

word = "Donkey"

with open("./04_Problem.txt", "r") as f:
    content = f.read()

contentNew = content.replace(word.lower(), "######")

with open("./04_Problem.txt", "w") as f:
    f.write(contentNew)