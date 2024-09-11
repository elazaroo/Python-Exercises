print("Highest number with functions")
print("------------------------------")

def compare():
    numbers = []
    for x in range(3):
        while True:
            try:
                choice = int(input("Insert one number: "))
                numbers.append(choice)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    
    if numbers[0] == numbers[1] == numbers[2]:
        print("All numbers are equal.")
    else:
        max_num = max(numbers)
        print("The max num is: ", max_num)

compare()