# my_info = {
#     'name': 'Big',
#     'age': 23,
#     'city': 'Bangkok'
# }

# my_name = my_info['name']
# print(my_name)
# my_age = my_info['age']
# print(my_age)
# print(type(my_age))

# my_info['city'] = 'New York'
# print(my_info)
# del my_info['age']
# print(my_info)

# for key in my_info:
#     print(key, ':', my_info[key])


# buy_list = ['Hobbit', 'Demon Slayer', 'Harry Potter', 'Demon Slayer']
# cost = 0
# for item in buy_list:
#     cost += book_cat[item] # book_cat['Hobbit'] = 300

# print("Total price = {}".format(cost))

# my_list = ['car', 'dog', 'bird', 'car', 'boy', 'boy']

# freq_dict = {}
# # freq_dict['car'] = 1 # Add key and value into dictionary
# for i in my_list:
#     if i in freq_dict:
#         freq_dict[i] += 1
#     else:
#         freq_dict[i] = 1
# print(freq_dict)




# freq_dict = {}
# for item in my_list:
#     if item in freq_dict:
#         freq_dict[item] += 1
#     else:
#         freq_dict[item] = 1

# print(freq_dict)







# cost = 0
# for i in  buy_list:
#     cost += book_cat[i]

# print('Total price = ', cost)


import matplotlib.pyplot as plt
book_dict = {
    'Hobbit': 300,
    'Harry Potter': 500,
    'The Lord' : 400,
    'Demon Slayer' : 200
}
# Extract keys and values from the dictionary
categories = list(book_dict.keys())
values = list(book_dict.values())
# Create a bar chart
plt.bar(categories, values, color='green')
# Set plot title and labels for axes
plt.title('Book Store Bar Chart')
plt.xlabel('Book name')
plt.ylabel('Price [Baht]')
# Customize tick labels and rotation
plt.xticks(rotation=45, ha='right')
# Show the plot
plt.tight_layout()
plt.show()