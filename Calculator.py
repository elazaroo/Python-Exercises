print("Eneko's calculator")

def operation():
    while True:
        print("What do you want to do?")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        choice = input("Enter choice: ")
        try:
            choice = int(choice)
            if choice in [1, 2, 3, 4]:
                match choice:
                    case 1:
                        return "add"
                    case 2:
                        return "sub"
                    case 3:
                        return "mult"
                    case 4:
                        return "div"
            else:
                print("Not valid choice. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def firstValue():
    while True:
        firstChoice = input("Insert first number: ")
        try:
            firstChoice = int(firstChoice)
            return firstChoice
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def secondValue():
    while True:
        secondChoice = input("Insert second number: ")
        try:
            secondChoice = int(secondChoice)
            return secondChoice
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def calculate(op, num1, num2):
    if op == "add":
        return num1 + num2
    elif op == "sub":
        return num1 - num2
    elif op == "mult":
        return num1 * num2
    elif op == "div":
        try:
            return num1 / num2
        except ZeroDivisionError:
            return "Cannot divide by zero"
    else:
        return "Invalid operation"

op = operation()
if op:
    num1 = firstValue()
    num2 = secondValue()
    result = calculate(op, num1, num2)
    print(f"The result is: {result}")