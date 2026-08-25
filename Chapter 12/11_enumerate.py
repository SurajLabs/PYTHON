l = [3, 34, 45, 56, 67]

# index = 0
# for item in l:
#     index += 1
#     print(f"The item number at index {index} is {item}")

# This can be simplified using the enumerate function as follows:

for index, item in enumerate(l):
    print(f"The item number at index {index} is {item}")