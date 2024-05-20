"""
1. Write a python script to multiple 2 or 3 or 4 numbers with a single
multiply method in a class using method overloading.

"""

class overloading:
    def add(self,num1,num2=None,num3=None):
        if num2 is None :
            return num1
        elif num3 is None:
            return num1+num2
        else:
            return num1+num2+num3
     

obj=overloading()
print(obj.add(2))
print(obj.add(2,3))
print(obj.add(2,3,4))