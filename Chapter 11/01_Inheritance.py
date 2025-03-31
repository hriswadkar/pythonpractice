
class Employee: #Parent Class
    company = "ICICI"

    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")


class Programmer(Employee): #Child class
    company = "ICICI Infotech"

    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")


a = Employee()
b = Programmer()


print(a.company, b.company)