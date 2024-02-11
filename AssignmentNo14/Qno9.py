"""
9. Write a Python script to print indices of all occurrences of a given element
in a given list.

"""

# Given list
my_list = [1, 2, 3, 2, 4, 5, 1, 3, 2, 5, 1, 3, 2]

# Given element
target_element = 2

# Find indices of occurrences of the target element
occurrence_indices = [index for index, element in enumerate(my_list) if element == target_element]

# Print indices of occurrences
print(f"Indices of occurrences of {target_element}: {occurrence_indices}")
