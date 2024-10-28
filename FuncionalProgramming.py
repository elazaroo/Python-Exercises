import random
from functools import reduce

# Generates a list of random numbers
def generate_random_list(size, lower_bound, upper_bound):
    return [random.randint(lower_bound, upper_bound) for _ in range(size)]

# Filters even numbers from the list
def filter_even_numbers(numbers):
    return list(filter(lambda x: x % 2 == 0, numbers))

# Maps numbers to their squares
def map_to_squares(numbers):
    return list(map(lambda x: x ** 2, numbers))

# Reduces the list by summing all elements
def sum_numbers(numbers):
    return reduce(lambda x, y: x + y, numbers)

def main():
    # Generate a list of 10 random numbers between 1 and 100
    random_list = generate_random_list(10, 1, 100)
    print("Random list:", random_list)

    # Filter even numbers
    even_numbers = filter_even_numbers(random_list)
    print("Even numbers:", even_numbers)

    # Map to squares
    squares = map_to_squares(even_numbers)
    print("Squares of even numbers:", squares)

    # Sum all squares
    total_sum = sum_numbers(squares)
    print("Sum of squares:", total_sum)

if __name__ == "__main__":
    main()