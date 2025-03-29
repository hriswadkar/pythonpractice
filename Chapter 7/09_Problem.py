# Write a program to print the following star pattern
'''
    * * *
    *   *
    * * *
'''

n = int(input("Enter a number: "))

for i in range(1, n+1):
    print("* " * n, end="") # end="" will not add a new line at the end of print statement
    print("")


# Harry's solution

for i in range(1, n+1):
    if (i == 1 or i == n):
        print("*" * n, end="")
    else:
        print("*", end="")
        print(" " * (n - 2), end="")
        print("*", end="")
    print("")