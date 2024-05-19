"""
4. Write a python script to update 2nd Question, add a class variable 
(platform) and create a classmethod to access it

"""
class Profile:

    platform='Python'

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

    #getter for eamil
    def get_email(self):
        return self.__email
    #setter for email
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
            raise ValueError("age must be postive") 

    @classmethod
    def get_class(cls):
        return cls.platform


obj=Profile("Vikash","vikash@gmail.com",23)

print(obj.get_name())
print(obj.get_email())
print(obj.get_age())

print(Profile.get_class())

obj.set_name("soumya")
obj.set_email("somuya@gmial.com")
obj.set_age(22)

print(obj.get_name())
print(obj.get_email())
print(obj.get_age())