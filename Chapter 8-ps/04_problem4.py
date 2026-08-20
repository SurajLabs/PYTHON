'''
sum(1) = 1
sum(2) = 1 + 2
sum(3) = 1 + 2 + 3
.
.
sum(n) = 1 + 2 + 3 + ... + n
sum(n) = sum(n-1) + n
'''
# RECURSIVE FUNCTION TO CALCULATE SUM OF FIRST N NATURAL NUMBERS

def sum(n):
    if n == 1:
        return 1
    else:
        return sum(n-1) + n
print(sum(3))