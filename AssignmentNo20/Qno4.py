"""
4. Write a python program to create a function that checks whether a passed string is
palindrome or not.

"""


def fuc_palindrome(str):
        return str ==str[::-1]
  



str=input("Enter a string here: ") 

ans=fuc_palindrome(str)

if ans:
    print("yes")
else:
    print("No")    