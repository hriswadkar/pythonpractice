# Write a program to print multiplication table of n using for loop in reverse order

num = int(input("Enter a number: "))

for i in range(10, 0, -1):
    print(f"{num} * {i} = {num * i}")