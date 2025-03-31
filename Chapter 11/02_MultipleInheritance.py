
class Employee: #Parent Class
    company = "ICICI"
    name = ""
    salary = 1200000

    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

class Coder:
    language = "Python"
    def printLanguages(self):
        print(f"Your default programming language is {self.language}")

class Programmer(Employee, Coder): #Child class inheriting from Employee and Coder
    company = "ICICI Infotech"

    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")


a = Employee()
b = Programmer()
b.name = "Harshad"
b.salary = 2600000


print(a.company, b.company)

b.show() # calling show method from Employee parent class
b.showLanguage() # calling method from Programmer class
b.printLanguages() # calling method from Coder parent class