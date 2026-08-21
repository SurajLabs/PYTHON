class employee:
    language = "Python" # class attribute
    salary = 1200000

harry = employee()
harry.name = "Harry" # instance attribute
print(harry.name, harry.language, harry.salary)

rohan = employee()
rohan.name = "Rohan"
print(rohan.name, rohan.language, rohan.salary)

# Here name is instance attribute and salary and language are class attributes as they directly belong to the class
