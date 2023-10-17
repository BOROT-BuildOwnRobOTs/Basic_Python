# a = [1,2,3,'abc',32.5,True]
# print(a)
# print(a[0]) # list[index]
# print(a[3])
# print(type(a))
# print(a[-2])
# a[3] = 'dfg'
# print(a)
# list_1 = [9,10,16,2,18]
# for i in list_1:
#     print(i)



# Excersise 4.1
# list_1 = [9,10,16,2,18]
# min = list_1[0]
# max = list_1[0]
# for i in list_1:
#     if i < min:
#         min = i
#         print('update min to {}'.format(min))
#     elif i > max:
#         max = i
#         print('update max to {}'.format(max))
# print('min = {}'.format(min))
# print('max = {}'.format(max))


# len(),min, max, sum\
'''
my_list = [1, 2, 33.2, 300]
print(len(my_list))
print(min(my_list))
print(max(my_list))
print(sum(my_list))
'''

# add in list
'''
my_list = [1, 2, 33.2, 300]
my_list.append(7)
print(my_list)
my_list.insert(0, 'cat')
print(my_list)
'''

# remove data in list
'''
my_list = [1, 2, 33.2, 300]
my_list.remove(33.2)
print(my_list)
my_list.pop()
print(my_list)
del my_list[0]
print(my_list)
my_list.clear()
print(my_list)
'''

# excercise 4.3
# my_list = [9,10,16,2,18,21,21,31,94,101,34,1,2,30,8,19]
# mean_value = sum(my_list)/len(my_list)
# print('mean is: ', mean_value)

# count_below = 0
# count_above = 0
# for i in my_list:
#     print('i = ', i)
#     if i < mean_value:
#         count_below += 1
#         print('i (lower avg) = ', i)
#     elif i > mean_value:
#         count_above += 1
#         print('i (greater avg) = ', i)
#     print('=========loop======')

# print('below mean are : ', count_below)
# print('above mean are : ', count_above)


# order in list
my_list = [3,7,8,3,1,5,12,54,7,21,5]
my_list.sort() # ascending
print(my_list)
my_list.reverse()# descending
print(my_list)
new_list = sorted(my_list) # ascending and can define new list
print(new_list)
new_list_2 = sorted(my_list ,reverse=True)# descending and can define new list
print(new_list_2)