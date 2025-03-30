# Write a function to print multiplication table of a given number

def MultiplicationTable(number):
    for i in range(1, 11):
        print(f"{number} * {i} = {number * i}")


n = int(input("Enter a number: "))

MultiplicationTable(n)