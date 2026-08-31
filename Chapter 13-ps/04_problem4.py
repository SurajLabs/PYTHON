def divisible5(n):
    if n % 5 == 0:
        return True
    return False
    
a = [1, 5, 10, 12, 15, 20, 22]

f = list(filter(divisible5, a))
print(f)

