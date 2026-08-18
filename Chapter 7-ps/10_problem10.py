# This program prints the table of a given number in reverse order using a for loop.

n = int(input("Enter the number: "))

for i in range(1, 11):
    print(f"{n} x {11-i} = {n*(11-i)}")
    

