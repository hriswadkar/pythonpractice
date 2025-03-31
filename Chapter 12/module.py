
def DivideTwoNumber(num1: int, num2: int) -> float:
    try:
        return (num1 / num2)
    except ZeroDivisionError as z:
        print("Division by zero not allowed")
    except ValueError as v:
        print("Invalid values provided for numbers")
    finally:
        print("Thank you for trying the function")

a: int = int(input("Enter number1: "))
b: int = int(input("Enter number2: "))

print("Calling DivideTwoNumber() function from module.py")
print(DivideTwoNumber(a, b))

print(__name__)

print("********************")