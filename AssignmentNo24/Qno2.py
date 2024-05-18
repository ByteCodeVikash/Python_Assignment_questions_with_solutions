#2. Write a python program to create a user class with a method to greet the user.

class user:
    def __init__(self,name):
        self.name=name

    def greet(self):
        print("hello",self.name,"!welcome")


obj1=user("Vikash")

obj1.greet()