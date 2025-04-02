# Write a list comprehension to print multiplication table of a user entered number


number = int(input("Enter a number: "))

tables = [number * i for i in range(1, 11)]
print(tables)

with open("multiplication.txt", "w") as f:
    f.write(str(tables))