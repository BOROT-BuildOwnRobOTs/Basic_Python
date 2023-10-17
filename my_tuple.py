my_tuple = (1,2,3,4)
# print(my_tuple[0])
# my_tuple[0] = 2 # error because can not modify

# slicing tuple
# print(my_tuple[0:2])

# unpacking tuple
a, b, c, d = my_tuple # a, b, c = my_tuple (can not)
# print(b)

# lenght
print(len(my_tuple))

# check statement
is_have = 1 in my_tuple
print(is_have)

# loop
for i in my_tuple:
    print(i)