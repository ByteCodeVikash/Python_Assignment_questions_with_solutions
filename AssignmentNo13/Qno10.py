"""
10. Write a Python script to create a list, where each element of the list is a
 digit of a given number.

"""

# Prompt user to enter a number
number = input("Enter a number: ")

# Create a list where each element is a digit of the given number
digits_list = [int(digit) for digit in number if digit.isdigit()]

print(digits_list)
