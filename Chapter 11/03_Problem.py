
class Employee:
    salary = 120000
    increment = 10

    @property
    def salaryAfterIncrement(self):
        return (self.salary + self.salary * (self.increment/100))
    
    @increment.setter
    def increment(self, value):
        self.increment = ((self.salary/self.salary) - 1) * 100



e = Employee()

print(e.salaryAfterIncrement)