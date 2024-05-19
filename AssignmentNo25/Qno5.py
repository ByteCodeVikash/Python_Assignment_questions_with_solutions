"""
5. Write a python script to create a Calculator class with 2 methods 
for adding and subtracting 2 values.

"""

class Calculator:

    def add(self,a,b):
        return a+b
    
    def sub(self,a,b):
        return a-b
    
cal=Calculator()

result_add=cal.add(3,4)
print("Result of addtion",result_add)

result_sub=cal.sub(4,2)
print("Result of sub",result_sub)