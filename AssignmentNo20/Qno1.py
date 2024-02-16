"""
1. Write a python program to create a function that takes a list and returns a new list
with the original list's unique elements

"""

def fuc(my_list):
    return list(set(my_list))


my_list=[1,2,3,4,5,1,3,5]
print("the unique elements of the list",fuc(my_list))
