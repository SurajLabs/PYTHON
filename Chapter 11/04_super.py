class Employee:
    def __init__(self):
        print("Constructor of Employee class")
    a = 1

class Programmer(Employee):
    def __init__(self):
        super().__init__() # Calls the constructor of Employee class
        print("Constructor of Programmer class")
    b = 2

class Manager(Programmer):
    def __init__(self):
        super().__init__() # Calls the constructor of Programmer class
        print("Constructor of Manager class")
    c = 3

# o = Employee()
# print(o.a)

# o = Programmer() 
# print(o.a, o.b)
 
o = Manager()
print(o.a, o.b, o.c) 