"""
10. Write a python program to create a function to check whether a string is an anagram
or not.
"""

def is_anagram(str1, str2):
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Check if the lengths of the strings are equal
    if len(str1) != len(str2):
        return False
    
    # Sort the characters in both strings and compare
    return sorted(str1) == sorted(str2)

# Example usage:
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if is_anagram(string1, string2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
