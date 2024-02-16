"""
9. Write a python program to create a function to check whether a string is a pangram
or not.

"""

import string

def is_pangram(sentence):
    alphabet = set(string.ascii_lowercase)
    # Convert the sentence to lowercase and remove non-alphabetic characters
    sentence_letters = set(filter(str.isalpha, sentence.lower()))
    return len(sentence_letters) == len(alphabet)

# Example usage:
sentence = input("Enter a sentence: ")
if is_pangram(sentence):
    print("The sentence is a pangram.")
else:
    print("The sentence is not a pangram.")
 