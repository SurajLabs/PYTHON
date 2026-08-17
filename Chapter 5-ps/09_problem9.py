s =  {8, 7, 12, "Haary", [1,2]}
s[4][0] = 9

# It is immutable and unhashable
# output: TypeError: unhashable type: 'list'
# we can not add list to set because list is mutable and unhashable.
# unhashable means that the object cannot be used as a key in a dictionary.