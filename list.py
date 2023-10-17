data = [9, 10, 16, 2, 18, 21, 21, 31, 94, 101, 34, 1, 2, 30, 8, 19]

# Calculate the mean
mean = sum(data) / len(data)

# Calculate the number of members below and above the average
below_average = 0
above_average = 0

for num in data:
    if num < mean:
        below_average += 1
    elif num > mean:
        above_average += 1

print("Mean:", mean)
print("Number of members below average:", below_average)
print("Number of members above average:", above_average)
