
n = int(input("Enter a number: "))

for i in range(1, n+1):
    print(("*" * i), end="") # end="" will not add a new line at the end of print statement
    print("")