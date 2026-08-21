class employee:
    language = "Python" # class attribute
    salary = 1200000

    def __init__(self, name, salary, language): # dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")
    def getinfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
    
    @staticmethod
    def greet():
        print("Good morning")

harry = employee("Harry", 1300000, "Javascript")
# harry.name = "Harry"
print(harry.name, harry.salary, harry.language)
