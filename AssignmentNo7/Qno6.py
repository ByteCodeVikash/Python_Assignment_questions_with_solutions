"""6. Write a python program to check whether a given string is a multiword string
 or single
word string using match case statement
"""


word=input("Enter here word: ")

match word:
    case w if ' ' in w:
        print("The given word is multiword")
    case _:
        print("The given word is singleword")    