import random

# Function to ask the user for the number of elements
def ask_number_of_elements():
    while True:
        try:
            n = int(input("Enter the number of elements: "))
            if n > 0:
                return n
            else:
                print("Please enter a number greater than 0.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

# Function to generate a list of names
def generate_name_list(n):
    name_list = []
    for i in range(n):
        name = input(f"Enter name {i+1}: ")
        name_list.append(name)
    return name_list

# Function to calculate the lengths of the names
def calculate_lengths(name_list):
    length_list = [len(name) for name in name_list]
    return length_list

# Function to generate a list of random DNIs
def generate_dni_list(name_list):
    dni_list = []
    for _ in name_list:
        dni = ''.join([str(random.randint(0, 9)) for _ in range(8)])
        dni_list.append(dni)
    return dni_list

# Function to generate a dictionary with DNIs as keys and names as values
def generate_dni_name_dict(name_list, dni_list):
    dni_name_dict = {dni: name for dni, name in zip(dni_list, name_list)}
    return dni_name_dict

# Function to search for a name by DNI in the dictionary
def search_name_by_dni(dni_name_dict, dni):
    return dni_name_dict.get(dni, "DNI not found")

# Function to calculate the mean of the lengths
def calculate_mean(length_list):
    return sum(length_list) / len(length_list)

# Function to calculate the variance of the lengths
def calculate_variance(length_list):
    mean = calculate_mean(length_list)
    variance = sum((x - mean) ** 2 for x in length_list) / len(length_list)
    return variance

# Function to save the data to a file
def save_data_to_file(name_list, dni_list, length_list, filename="data.txt"):
    with open(filename, 'w') as file:
        for name, dni, length in zip(name_list, dni_list, length_list):
            file.write(f"{name},{dni},{length}\n")

# Main function to coordinate the execution of the program
def main():
    n = ask_number_of_elements()
    name_list = generate_name_list(n)
    length_list = calculate_lengths(name_list)
    dni_list = generate_dni_list(name_list)
    dni_name_dict = generate_dni_name_dict(name_list, dni_list)
    print("List of names:", name_list)
    print("Lengths of names:", length_list)
    print("List of DNIs:", dni_list)
    print("DNI-Name Dictionary:", dni_name_dict)
    
    dni_to_search = input("Enter the DNI to search: ")
    name = search_name_by_dni(dni_name_dict, dni_to_search)
    print(f"Name corresponding to DNI {dni_to_search}: {name}")
    
    mean = calculate_mean(length_list)
    variance = calculate_variance(length_list)
    print(f"Mean of lengths: {mean}")
    print(f"Variance of lengths: {variance}")
    
    save_data_to_file(name_list, dni_list, length_list)
    print("Data saved to 'data.txt'.")

if __name__ == "__main__":
    main()