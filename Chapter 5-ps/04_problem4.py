s = set()
s. add(20)
s. add(20.0) # set will not allow duplicate values, so 20.0 will not be added because 20 and 20.0 are considered equal in Python.
s.add('20') # length of s after these operations?
print(s)
print(len(s))
