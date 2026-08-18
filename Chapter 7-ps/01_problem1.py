# This program prints the table of a given number using a for loop.

n = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i} ")
    