"""
3. Write a python program to create a function that prints the even numbers from a
given list.
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]

"""

def even_no(my_list):
    for i in my_list:
        if i%2==0:
            print(i,"is even number")
        




my_list=[1,2,3,4,5,6,7,8,9]

even_no(my_list)