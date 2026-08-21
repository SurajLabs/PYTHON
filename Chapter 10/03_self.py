class employee:
    language = "Python" # class attribute
    salary = 1200000

    def getinfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
    
    @staticmethod
    def greet():
        print("Good morning")

harry = employee()
# harry.language  = "JavaScript" # instance attribute
harry.greet()
harry.getinfo()
# employee.getinfo(harry)
