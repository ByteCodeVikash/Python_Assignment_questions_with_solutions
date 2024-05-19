"""
7. Write a python script to create a Phone class with 2 methods to
print the features (calling and sms).

"""

class Phone:

    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def call(self):
        print("call features on",self.brand,self.model)

    def sms(self):
        print("sms featurs on",self.brand,self.model)

obj=Phone("iphone","iphone12")

obj.call()
obj.sms()
        