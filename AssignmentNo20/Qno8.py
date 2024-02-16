"""
8. Write a python program to create a function that accepts a string and calculate the
number of upper case letters and lower case letters.

"""

def count_upper_lower(text):
    upper_count = 0
    lower_count = 0
    for char in text:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    return upper_count, lower_count

text = input("Enter a string here: ")
upper, lower = count_upper_lower(text)
print("Number of uppercase letters:", upper)
print("Number of lowercase letters:", lower)

