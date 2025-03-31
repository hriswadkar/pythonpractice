
class MyClass:
    num = 1

    @classmethod
    def printNumber(self):
        print(f"Number is {self.num}")


obj = MyClass()
obj.num = 100

obj.printNumber()