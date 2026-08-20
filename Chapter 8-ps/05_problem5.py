# RECURSIVE FUNCTION TO PRINT A PATTERN OF STARS
def pattern(n):
    if n == 0:
        return
    print("*" * n)
    pattern(n - 1)

pattern(5)