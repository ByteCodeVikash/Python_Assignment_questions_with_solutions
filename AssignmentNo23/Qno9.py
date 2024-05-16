"""
9. Define a function which takes lengths of three sides of a triangle
as arguments and display the perimeter or triangle. Define and apply a
decorator which checks for the validity of the triangle on the basis of
lengths of the side. This makes the perimeter to be displayed when the 
triangle can exist with the given lengths of the sides.

"""


def check_triangle_validity(func):
    def wrapper(a,b,c):
        if a+b>c and b+c>a and a+c>b:
            return func(a,b,c)
        else:
            print("Invalid triangle ! the given side length cannot form a triangle")
    return wrapper


@check_triangle_validity
def calculate_per(a,b,c):
    perimenter=a+b+c
    print("Perimeter of the triangle:",perimenter)

calculate_per(2,3,4)
calculate_per(1,2,3)    

