print("MaxNum")

def compare():
    max_num = None
    for x in range(3):
        while True:
            try:
                choice = int(input("Insert one number: "))
                if max_num is None or choice > max_num:
                    max_num = choice
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    print("The max num is: ", max_num)

compare()