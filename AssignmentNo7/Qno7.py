"""7. Write a python program to check whether a given number is positive, 
negative or
zero using match case statement
"""

num=int(input("Enter a number here: "))

match num:
    case num if num>0:
        print("postive")
    case num if num<0:
        print("negative")
    case _:
        print("zero")        