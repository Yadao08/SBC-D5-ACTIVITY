print("CORRUPT OFFICES")

list = [] # initialize

#mag ask ug 5 values from the user gamit ang for loop
for i in range(5):
    added_val = input(f"Add your values in list {i + 1}: ") #mag iterate
    list.append(added_val)  # eh append diri ang value sa list

# Prompt the user to enter either 0 or 1, indicating the boss's presence
print("Enter 0 for 'naa' or 1 for 'wala' ")
head = int(input("Is Boss around?: "))

# Check if the input is 0
if head == 0:
    list.pop(0)  # Remove the first element from the list
    print("The values you inputted are: ", list)  # Print the modified or updated na list
    print("----------------------------")
    # Gather 2 new values from the user then append it to the list
    for i in range(2):
        new = input(f"New Value added {i + 1}: ")
        list.append(new)
    print("----------------------------")
    print("Your Updated Lists: ", list)  # Print the updated list

# Check if the input is 1/same process in 0
elif head == 1:
    list.pop()
    print("The values you inputted are: ", list)
    print("----------------------------")
    for i in range(2):
        new = input(f"New Value added {i + 1}: ")
        list.append(new)
    print("----------------------------")
    print("Your Updated Lists: ", list)
else:
    print("Error 500, Run it again!")
