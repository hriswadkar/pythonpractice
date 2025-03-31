# Create a class "Programmer" for storing information of few programmers working at Microsoft

class Programmer:
    name = ""
    language = ""
    company = ""

    def __init__(self, name, language, company):
        print("initializing")
        self.name = name
        self.language = language
        self.company = company

    def getInfo(self):
        print(f"Name: {self.name}, Language: {self.language}, Company: {self.company}")


ScottG = Programmer("Scott Guthrie", "ASP.NET MVC", "Microsoft")

print(ScottG.getInfo())