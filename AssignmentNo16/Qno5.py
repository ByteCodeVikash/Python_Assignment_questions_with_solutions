#5. Write a python program to check if all items in the tuple are the same.

# Define a tuple
my_tuple = (4, 4, 4, 4)

# Flag to track if all items are the same
all_same = True

# Iterate over the tuple starting from the second element
for item in my_tuple[1:]:
    # If any element is not equal to the first element, set flag to False and break the loop
    if item != my_tuple[0]:
        all_same = False
        break

# Check if all items are the same
if all_same:
    print("All items in the tuple are the same.")
else:
    print("Not all items in the tuple are the same.")
