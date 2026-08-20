# REMOVE A WORD OR ATTACHED WORD FROM A LIST

def rem(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n

l = ["Harry", "Sally", "Crayon", "Lucy", "Brandon", "on" ]
print(rem(l, "on"))
