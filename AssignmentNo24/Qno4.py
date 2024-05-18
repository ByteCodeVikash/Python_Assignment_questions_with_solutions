#4. Write a python program to init default values for user object using __init__ method.



class User:
    def __init__(self,name="Vikash",age=23):
        self.name=name
        self.age=age


obj1=User()
print("name: ",obj1.name,"age: ",obj1.age)