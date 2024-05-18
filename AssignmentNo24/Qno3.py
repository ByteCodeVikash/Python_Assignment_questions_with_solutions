"""3. 
Write a python program to create 2 objects of the user class and assign
different values.

"""

class User:
    def __init__(self,a,b):
        self.a=a
        self.b=b


obj1=User(2,3)
obj2=User(4,5)

print(obj1.a,obj1.b)
print(obj2.a,obj2.b)