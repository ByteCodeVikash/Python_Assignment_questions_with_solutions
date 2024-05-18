#1. Write a python program to create a user class with 3 properties : name, age, email.


class User:
    name="Vikash"
    age=24
    email="vikash@gmail.com"

    


obj1=User()
print(obj1.name)
print(obj1.age)
print(obj1.email)


# second method using instance vaiable

class user:
    def __init__(self,name,age,email):
        self.name=name
        self.age=age
        self.email=email


obj1=user("Vikash",23,"vikash@gmail.com")

print(obj1.name)
print(obj1.age)
print(obj1.email)