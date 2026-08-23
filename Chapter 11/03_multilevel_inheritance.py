class Employee:
    a = 1

class Programmer(Employee):
    b = 2

class Manager(Programmer):
    c = 3

o = Employee()
print(o.a) # Prints the a attribute
# print(o.b) # Shows an error as there is no b attribute in Employee class
o = Programmer()
print(o.a, o.b) # Prints the a and b attribute
o = Manager()
print(o.a, o.b, o.c) # Prints the a, b and c attribute