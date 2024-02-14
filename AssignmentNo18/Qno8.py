"""
8. Write a python program to convert two lists into a dictionary in a way that item from
list1 is the key and item from list2 is the value.
"""

list1=[1,2,3,4]
list2=['a','b','c','d']

my_dict=dict(zip(list1,list2))

print(my_dict)