"""
8. Write a python script to create a SmartPhone class by inheriting Calculator
 2.0 and Phone Class.

"""

class Calculator:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
class Calculator2(Calculator):
    def mul(self,a,b):
        return a*b 
    def div(self,a,b):
        return a/b
class Phone:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def call(self):
        print("call features on",self.brand,self.model)
    def sms(self):
        print("sms feature on ",self.brand,self.model)

class SmartPhone(Calculator2,Phone):
    def __init__(self,brand,model):
        Calculator2.__init__(self)
        Phone.__init__(self,brand,model)

my_smartphone=SmartPhone("Apple","iphone12")

print("Result of multipliction",my_smartphone.mul(2,3))
print("Result of devision",my_smartphone.div(6,2))

my_smartphone.call()
my_smartphone.sms()