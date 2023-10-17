# Set in Python
# my_set = {10,20,30,30,30,30}
# print(my_set)

# my_set.add(40)
# print(my_set)
# my_set.update({50,60,70,70})
# print(my_set)

# my_set.remove(40)
# print('removed : ', my_set)
# my_set.discard(50)
# print('discarded : ', my_set)
# my_set.discard(100)
# # my_set.remove(100)

set1 = {1,2,3,}
set2 = {3,4,5}
u_set = set1.union(set2)
i_set = set1.intersection(set2)
d_set = set1.difference(set2)
print(u_set)
print(i_set)
print(d_set)