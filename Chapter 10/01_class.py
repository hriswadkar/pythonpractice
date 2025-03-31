class Employee:
    name = "Harshad"
    language = "Python"
    salary = 200000

    def __init__(self):
        print("Object is created")

    def getInfo(self): # keyword self needs to be given in the method parameter
        print(f"Name: {self.name}; Language: {self.language}; Salary: {self.salary}")

harshad = Employee()
harshad.getInfo()
harshad.language = "Java"
harshad.getInfo()


print(harshad.name + ", " + harshad.language + ", " + str(harshad.salary))