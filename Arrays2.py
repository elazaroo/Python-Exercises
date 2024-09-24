import random

def generate_array(size):
    """Generate an array of random integers."""
    return [random.randint(0, 100) for _ in range(size)]

def linear_search(array, element):
    """Linear search  in the array."""
    for index, value in enumerate(array):
        if value == element:
            return index
    return -1

def binary_search_recursive(array, element, low, high):
    """Binary search recursively."""
    if low > high:
        return -1
    mid = (low + high) // 2
    if array[mid] == element:
        return mid
    elif array[mid] < element:
        return binary_search_recursive(array, element, mid + 1, high)
    else:
        return binary_search_recursive(array, element, low, mid - 1)

def sort_array(array, method):
    """Sort the array using X method."""
    if method == 1:
        # Bubble sort method
        size = len(array)
        for i in range(size):
            for j in range(0, size - i - 1):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
    elif method == 2:
        # sort() method
        array.sort()
    elif method == 3:
        # sorted() method
        array = sorted(array)
    return array

def main():
    # 1. Generate the size of the array
    size = None
    while size is None:
        try:
            size = int(input("Insert the size of the array: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

    # 2. Generate the array of random elements
    array = generate_array(size)
    print("Generated array:", array)
    print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

    # 3. Search using linear search
    while True:
        try:
            element = int(input("Insert the element you want to search: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    position = linear_search(array, element)
    if position != -1:
        print("Element found at position:", position)
    else:
        print("Element not found.")
    print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

    # 4. Sort the array with chosen method
    print("1. Bubble sort method\n2. sort() method\n3. sorted() method\n")
    while True:
        try:
            method = int(input("Which method do you want to use? "))
            if method in [1, 2, 3]:
                array = sort_array(array, method)
                print("Sorted array:", array)
                break
            else:
                print("Invalid input. Please enter a valid number (1, 2, or 3).")
        except ValueError:
            print("Invalid input. Please enter a valid number (1, 2, or 3).")
    print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

    # 5. Search using linear search in the sorted array
    while True:
        try:
            element = int(input("Insert the element you want to search: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    position = linear_search(array, element)
    if position != -1:
        print("Element found at position:", position)
    else:
        print("Element not found.")
    print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

    # 6. Search using binary search in the sorted array
    while True:
        try:
            element = int(input("Insert the element you want to search: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    position = binary_search_recursive(array, element, 0, size - 1)
    if position != -1:
        print("Element found at position:", position)
    else:
        print("Element not found.")
    print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")


main()