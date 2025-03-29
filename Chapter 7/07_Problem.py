# Write a program to print star pattern

for i in range(1, 6):
    print("*" * i)


n = int(input("Enter a number: "))

for i in range(1, n+1):
    print(" " * (n-i), end="") # end="" will not add a new line at the end of print statement
    print("*" * (2 * i - 1), end="")
    print("\n")


for i in range(1, n+1):
    print(" " * (n-i) + ("*" * (2 * i - 1)), end="") # end="" will not add a new line at the end of print statement
    print("")