# print multiplication table of a given number using while loop

num = int(input("Enter a number: "))

counter = 1

while (counter <= 10):
    print(f"{num} * {counter} = {num * counter}")
    counter += 1
