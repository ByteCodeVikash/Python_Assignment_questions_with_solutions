"""
3. Write a python program to create a function which expects an unknown number of
arguments.

"""

def fuc(*args):
    total=sum(args)
    print("sum of all arguments",total)

fuc(3,2)
fuc(4,5,6,7)