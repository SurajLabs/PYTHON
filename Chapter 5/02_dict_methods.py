marks = {
    "Harry": 100,
    "Shubham": 56,
    "Rohan": 34

}

print(marks.items()) # it will return a list of tuples
print(marks.values()) # it will return a list of values
print(marks.keys()) # it will return a list of keys
marks.update({"Harry": 99}) # updates the value of "Harry"
print(marks) # {'Harry': 99, 'Shubham': 56, 'Rohan': 34}
print(marks.get("Harry")) # output: 99
print(marks["Harry"]) # output: 99
