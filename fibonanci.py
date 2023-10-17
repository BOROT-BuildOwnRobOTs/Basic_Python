def generate_fibonacci(n):
    fibonacci_sequence = [0, 1]  # Initialize with the first two Fibonacci numbers
    for i in range(2, n):
        next_fibonacci = fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2]
        fibonacci_sequence.append(next_fibonacci)
    return fibonacci_sequence

try:
    n = int(input("Enter the number of Fibonacci numbers to generate: "))
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        fibonacci_numbers = generate_fibonacci(n)
        print("Fibonacci sequence:", fibonacci_numbers)
except ValueError:
    print("Invalid input. Please enter a valid positive integer.")