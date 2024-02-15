"""
9. Write a python program to create a function to check whether a number falls in a
given range.

"""

def check_range(number, lower_bound, upper_bound):
    return lower_bound <= number <= upper_bound

# Example usage
number_to_check = 5
lower_bound = 1
upper_bound = 10

if check_range(number_to_check, lower_bound, upper_bound):
    print(f"{number_to_check} falls within the range [{lower_bound}, {upper_bound}]")
else:
    print(f"{number_to_check} does not fall within the range [{lower_bound}, {upper_bound}]")
