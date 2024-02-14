"""
10. Write a python program to get the key of lowest value from the dictionary.
sample_dict = {
'C': 92,
'Java': 66,
'Python': 85
}

"""

sample_dict = {
    'C': 92,
    'Java': 66,
    'Python': 85
}

min_value = float('inf')  # Initialize min_value to positive infinity
min_key = None

for key, value in sample_dict.items():
    if value < min_value:
        min_value = value
        min_key = key

print("Key of the lowest value:", min_key)
