
class GrandFather:
    surname = "Riswadkar"
    placeOfOrigin = "Riswad"
    name = "Ramchandra"
    
    def __init__(self):
        print(f"Name is {self.name}, Surname is {self.surname} and place of origin is {self.placeOfOrigin}")

    def getSurname(self):
        print(f"Surname is {self.surname}")

class Father(GrandFather):
    profession = "Draftsman"

    def __init__(self):
        super().__init__()
        self.name = "Ravindra"
        print(f"Name is {self.name}, Surname is {self.surname} and profession is {self.profession}")

class Son(Father):
    profession = "Tech Lead"
    hobby = "Photography"

    def __init__(self):
        super().__init__()
        self.name = "Harshad"
        print(f"Name is {self.name}, Surname is {self.surname} and profession is {self.profession}. Hobby is {self.hobby}")


ramchadra = GrandFather()
ravindra = Father()
harshad = Son()

