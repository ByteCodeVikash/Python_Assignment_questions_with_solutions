"""
3. Write a python script to update 2nd Question, change email and age
to __email and __age.

"""

class Profile:

    def __init__(self,name,email,age):
        self.__name=name
        self.__email=email
        self.__age=age


    #getter for name
    def get_name(self):
        return self.__name   
    #setter for name
    def set_name(self,name):
        self.__name=name

    #getter for email
    def get_email(self):
        return self.__email 

    #setter for eamil
    def set_email(self,email):
        self.__email=email    

    #getter for age 
    def get_age(self):
        return self.__age

    #setter for age
    def set_age(self,age):
        if age>0:
            self.__age=age
        else:
            raise ValueError("Age must be postive")


obj=Profile("Vikash","Vikash@gmail.com",23)

print(obj.get_name())
print(obj.get_email())
print(obj.get_age())

obj.set_name("jalaj")
obj.set_email("jalaj@gmail.com")
obj.set_age(22)

print(obj.get_name())
print(obj.get_email())
print(obj.get_age())
