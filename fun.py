def printSomething():
    print('Test function.')

def addValue(x,y):
    ans = x+y
    print(ans)

def money(x):
    x=100
    print('Local : ', x)

x = 50
# print('Global : ', x)
# money(x)

# def addValuereturn(x,y):
#     ans = x+y
#     return ans

# addValuereturn(10,20)
# print('return is value = ', addValuereturn(10,20))
import math
def circle_func(radius):
    area = math.pi*(radius**2)
    return area
# print(circle_func(3))

def findEven(list_input):
    even_list = []
    for i in list_input:
        if (i % 2 == 0) and (i != 0):
            even_list.append(i)
    print(even_list)

# findEven([4,6,2,324,65,768,0,3,7,0,4])

def generate_fibonacci(n):
    n = int(n)
    fibonacci_sequence = [0, 1]  # Initialize with the first two Fibonacci numbers
    if n <= 0:
        return "Please insert positive integer"
    elif n == 1:
        return [0]
    elif n == 2:
        return [0,1]
    else:
        for i in range(2, n):
            next_fibonacci = fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2]
            fibonacci_sequence.append(next_fibonacci)
        return fibonacci_sequence

n_terms = 30
fibonacci_numbers = generate_fibonacci(n_terms)
print("Fibonacci sequence:", fibonacci_numbers)

# import matplotlib.pyplot as plt
# plt.plot(fibonacci_numbers, marker='o')
# plt.title(f"Fibonacci Sequence (First {n_terms} terms)")
# plt.xlabel("Term Index")
# plt.ylabel("Fibonacci Number")
# plt.grid(True)
# plt.show()








#     even_list = []
#     for i in list:
#         if (i % 2 == 0) and (i != 0):
#             even_list.append(i)
#     return even_list

# print(findEven([4,6,2,324,65,768,0,3,7,0,4]))