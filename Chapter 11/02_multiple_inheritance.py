from random import randint
class Employee:
    company = "ITC"
    name = "John Doe"
    salary = randint(10, 20)*5000
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

class Coder:
    language = "Python"
    def printLanguage(self):
        print(f"Out of your languages here is your language:{self.language}")


class Programmer(Employee, Coder): # Multiple Inheritance
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self. language} language")

a = Employee()
b = Programmer()

b.show()
b.printLanguage()
b.showLanguage()
