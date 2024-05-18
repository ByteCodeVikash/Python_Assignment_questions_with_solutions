#6. Write a python program to create 3 user objects and find the youngest of all
class User:
    def __init__(self,age):
        self.age=age
        



obj1=User(23)
obj2=User(30)
obj3=User(28)

if obj1.age>obj2.age and obj1.age>obj3.age:
    print(obj1.age,"is youngest")
elif obj2.age>obj1.age and obj2.age>obj3.age:
    print(obj2.age,"is the youngest")
else:
    print(obj3.age,"is younger")        
