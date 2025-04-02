
class Person:
    FirstName = ""
    LastName = ""
    City = ""

    def __init__(s, firstName, lastName, city):
        s.FirstName = firstName
        s.LastName = lastName
        s.City = city

    def getPersonInfo(s):
        print("***** User Info *****")
        print(f"{s.FirstName}, {s.LastName}, {s.City}")


p1 = Person("Harshad", "Riswadkar", "City")

print(p1.getPersonInfo())
        