#1. Write a python script to create a Profile class with 3 attributes (name, email, age).


class Profile:
    def __init__(self,name,email,age):
        self.name=name
        self.email=email
        self.age=age


obj=Profile("Vikash","vikash@gmail.com",23)

print(obj.name)
print(obj.email)
print(obj.age)