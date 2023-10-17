# # while loop
# i = 1
# while i<=3:
#     print(i)
#     i += 1
# print('==========================================================')
# # for loop
# for j in range(1,4,1):
#     print(j)

# start_value = int(input('num start: '))
# end_value = int(input('num end: '))
# print('start at {}'.format(start_value))
# print('stop at {}'.format(end_value))
# while start_value <= end_value:
#     print('number of loop = {}'.format(start_value))
#     start_value += 1
# print('End')

# excercise 3.1
# num = int(input('num of countdown = '))
# while num>=0:
#     print(num)
#     num -= 1
# print('Finish')

# for i in range(num, -1, -1):
#     print(i)
# print('Finish')

# excercise 3.2
head = int(input('head of multiplication table = '))
num = int(input('num of time = '))

for i in range(1, num+1):
    cal = head*i
    print('{} x {} = {}'.format(head, i, cal))