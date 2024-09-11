print("Highest number without functions")
print("---------------------------------")

i = [None, None, None]

for x in range(3):
    while True:
        cont = "i" + str(x)
        i[x] = input("Insert a number (" + str(x+1) + "): ")
        if i[x].isdigit():
            i[x] = int(i[x])
            break
        else:
            print("Please enter a valid number.")
            
if i[0] == i[1] == i[2]:
    print("All numbers are equal.")
else:
    max = i[0]
    for w in range(2):
        if i[int(w+1)] > max:
            max = i[int(w+1)]
    print("The highest number is: ", max)