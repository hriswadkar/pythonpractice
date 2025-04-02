
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print(a/b)
except ZeroDivisionError as z:
    print("Division by zero is not allowed")
except ValueError as v:
    print("Incorrect input")