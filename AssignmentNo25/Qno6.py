"""
6. Write a python script to create a Calculator 2.0 class with 2 methods
for multiplication and division of 2 values and inherit it from the Calculator 
class.

"""

class Calculator:
    def add(self,a,b):
        return a+b
    
    def sub(self,a,b):
        return a-b
    
class Calculator2(Calculator):

    def mul(self,a,b):
        return a*b
    
    def div(self,a,b):
        return a/b

cal=Calculator2()


print("this is add result",cal.add(3,4))
print("this is substraction",cal.sub(4,2))
print("this is multi",cal.mul(2,3))
print("this is div",cal.div(6,2))
