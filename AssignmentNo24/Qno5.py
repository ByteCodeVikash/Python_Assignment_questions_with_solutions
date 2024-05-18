#5. Write a python program to delete the age property of the user


class User:
    def __init__(self,name,age):
        self.name=name
        self.age=age

obj=User("Vikash",23)

del obj.age

try:
    print(obj.age)
except AttributeError:
    print("the age property has been deleted")    