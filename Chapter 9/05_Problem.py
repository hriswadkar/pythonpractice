# A file contains word "Donkey". Write a program that replaces the word donkey with ###### and update it in the file

words = ["Donkey", "Swine"]

with open("./05_Problem.txt", "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, ("#" * len(word)))

with open("./05_Problem.txt", "w") as f:
    f.write(content)