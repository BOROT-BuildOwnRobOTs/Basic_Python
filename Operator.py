# x = 10
# y = 20

# result_a = x + y
# print(result_a)

# y = '20'
# # result_b = x + y
# # print(result_b)
# print(type(y))
# result_b = x + int(y)
# print(type(int(y)))
# print(result_b)

# name = 'Tharittapol'
# surname = 'Takhumsuk'
# fullname = name + surname
# print(fullname)

# x = '20'
# y = '23'
# ans = x+y
# print(ans)

# a = 1 + 3 * 4
# print(a)
# add parentheses
# b = (1 + 3) * 4
# print(b)
# c = 9
# d = 2
# result_c = c % d
# print(result_c)
# result_d = c ** d
# print(result_d)
# result_e = c // d
# print(result_e)

# exercise 1
'''
age = input("How old are you? ")
print(age)
print('I am ' + age + ' years old')
print('I am {} years old and My name is {}{}'.format(age, 'Big', '!'))
'''
# print(type(age))

# exercise 2
'''
value_a = input('a : ')
value_b = int(input('b : '))
result = int(value_a) + value_b
print(result)
'''

# exercise 3
'''
a = int(input('value in cm : '))
ans = a/100
print('convert {} cm to metre {} m'.format(a, ans))
'''

# exercise 4
'''
a = float(input('celsius " '))
ans = a*9/5 + 32
print(ans)
print(type(ans))
'''

# x = 5
# x = x+1
# x += 1
# print(x)

# x = 25
# if x>=13 and x<20:
#     print('Teenager')
# elif x>=20:
#     print('Youth')
# else:
#     print('Child')
# print('End')

# excercise 2.1
# import math
# score = float(input('Your score is : '))
# scoreA = math.ceil(score)
# print(scoreA)
# scoreB = math.floor(score)
# print(scoreB)
# # must insert value in 0 to 100
# if 0<=score<=100: # is mean score >=0 and score <= 100.
#     if score>=80:
#         print('Grade A')
#     elif score>=60 and score<80:
#         print('Grade B')
#     elif score>=40 and score<60:
#         print('Grade C')
#     elif score>=20 and score<40:
#         print('Grade D')
#     else:
#         print('Grade F')
# else:
#     print('Please in put score in range 0 to 100')

# excersise 2.2
mode = str(input('Please select mode: '))
# if mode == 'F->C':
if mode in 'F->C':
    temp = float(input('Your temp is : '))
    print(5*(temp-32)/9)
elif mode == 'C->F':
    temp = float(input('Your temp is : '))
    print(9*temp/5 + 32)
else:
    print('Wrong mode')

