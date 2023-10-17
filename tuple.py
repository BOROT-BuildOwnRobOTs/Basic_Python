# Creating a tuple
my_tuple = (1, 2, 'three', True, 3.5)

# Accessing elements by index
first_element = my_tuple[0]
second_element = my_tuple[1]

print("First Element:", first_element)
print("Second Element:", second_element)

#######################################################################

# Slicing a tuple
slice_tuple = my_tuple[1:4]  # Slicing from index 1 to 3 (excluding 4)
print("Sliced Tuple:", slice_tuple)  # Output: (2, 3, 4)

# Tuple unpacking
a, b, c, d, e = my_tuple
print("Unpacked Values:", a, b, c, d, e)  # Output: 1 2 3 4 5

# Length of a tuple
tuple_length = len(my_tuple)
print("Tuple Length:", tuple_length)  # Output: 5

# Checking if an element exists in a tuple
element_exists = 3 in my_tuple
print("Element 3 exists:", element_exists)  # Output: True

# Iterating through a tuple
for item in range(len(my_tuple)):
    print(item)
for item in my_tuple:
    print(item)