# Write a class "calculator" capable of finding square, cube and square root of a number
import math

class Calculator:
    number = 0

    def __init__(self, num):
        self.number = num

    def getSquare(self):
        return self.number * self.number
    
    def getSquare2(self):
        return self.number ** 2
    
    def getCube(self):
        return self.number * self.number * self.number
    
    def getSquareRoot(self):
        return int(math.sqrt(self.number))
    
    def getSquareRoot2(self):
        return int(self.number ** 1/2)
        

n = int(input("Enter a number: "))
calc = Calculator(n)

print(calc.getSquare())
print(calc.getCube())
print(calc.getSquareRoot())

print("Alternate methods")
print(calc.getSquareRoot2())
print(calc.getSquare2())