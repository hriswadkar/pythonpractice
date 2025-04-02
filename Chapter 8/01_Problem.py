
def FindGreatestNumber(number1, number2, number3):
    message = ""
    if (number1 > number2 and number1 > number3):
        message = f"{number1} is highest"
    elif (number2 > number1 and number2 > number3):
        message = f"{number2} is highest"
    else:
        message = f"{number3} is highest"

    return message

num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))
num3 = int(input("Enter number3: "))


result = FindGreatestNumber(num1, num2, num3)

print(result)