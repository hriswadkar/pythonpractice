from module import DivideTwoNumber

a1: int = int(input("Enter one number: "))
a2: int = int(input("Enter another number: "))

print("Calling DivideTwoNumber() function from main.py")

print(DivideTwoNumber(a1, a2))
print(__name__)