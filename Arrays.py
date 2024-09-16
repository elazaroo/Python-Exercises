""" 1. Allow the user to enter the number of elements in the array. """
size = None
while size is None:
    try:
        size = int(input("Insert the size of the array: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

""" 2. Allow the user to enter the array elements """
array = []
for x in range(size):
    while True:
        try:
            choice = int(input("Insert one number: "))
            array.append(choice)
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

""" 3. Search for an item (entered by the user) with linear search """
while True:
    try:
        element = int(input("Insert the element you want to search: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")
for x in range(size):
    if array[x] == element:
        print("Element found at position: ", x)
        break
else:
    print("Element not found.")
print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")


""" 4. Sort the array. Several methods can be implemented """
print("1. Bubble sort method\n2. sort() method\n3.sorted() method\n")
while True:
    try:
        method = int(input("Which method do you want to use?"))
        if method in [1, 2, 3]:
            match method:
                case 1:
                    # Bubble sort method
                    for x in range(size):
                        for y in range(size):
                            if array[x] < array[y]:
                                array[x], array[y] = array[y], array[x]
                    print("Array sorted: ", array)
                case 2:
                    # sort() method
                    array.sort()
                    print("Array sorted: ", array)
                case 3:
                    # sorted() method
                    array = sorted(array)
                    print("Array sorted: ", array)
            break
        else:
            print("Invalid input. Please enter a valid number (1, 2, or 3).")
    except ValueError:
        print("Invalid input. Please enter a valid number (1, 2, or 3).")
print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

""" 5. Search for an item (entered by the user) with linear search knowing that it is sorted """
while True:
    try:
        element = int(input("Insert the element you want to search: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")
for x in range(size):
    if array[x] == element:
        print("Element found at position: ", x)
        break
else:
    print("Element not found.")
print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

""" 6. Search for an item (entered by the user) with binary search knowing that it is sorted """
while True:
    try:
        element = int(input("Insert the element you want to search: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")
low = 0
high = size - 1
while low <= high:
    mid = (low + high) // 2
    if array[mid] == element:
        print("Element found at position: ", mid)
        break
    elif array[mid] < element:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Element not found.")