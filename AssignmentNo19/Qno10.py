"""
10. Write a python program to create a function to check whether a given number is even
or odd.


"""


def fuc_check(input_num):
    if input_num%2==0:
        print("this is even no.")
    else:
        print("this is odd numbere")    
    
num=int(input("Enter a number here: "))
fuc_check(num)