# Write a program to calculate factorial of a given number using for loop

import math

num = int(input("Enter a number: "))
product = 1;

if (num >= 0):
    for i in range (1, num+1):
        product *= i

print(f"product is {product}")

print("using another way of for loop")
product = 1

if (num >= 0):
    for i in range (num+1):
        if (i == 0):
            continue
        product *= i

print(f"product is {product}")

print("Getting factorial using math.factorial() method")

print(math.factorial(num))