"""
10. Write a python script to add the new method in SmartPhone class 
which accepts Truecaller object as a parameter and call the fetch method
of Truecaller.

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
        print("call feature",self.brand,self.model)

    def sms(self):
        print("sms feature",self.brand,self.model) 

class SmartPhone(Calculator2,Phone):
    def __init__(self,brand,model):
        Calculator2.__init__(self)
        Phone.__init__(self,brand,model)

    def fetch_from_truecaller(self,truecaller,number):
        name=truecaller.fetch_name(number)
        print("name for",number,"retrieved from TrurCaller",name)


my_smartphone=SmartPhone("Apple","iphone12")

class Truecaller:
    def __init__(self):
        self.contacts={"+12234456789":"vikash","+69839882589":"shivam"}

    def fetch_name(self,number):
        if number in self.contacts:
            return self.contacts[number]
        else:
            return "Name not found for this number" 

Truecaller_app=Truecaller()

my_smartphone.fetch_from_truecaller(Truecaller_app,"+12234456789")
my_smartphone.fetch_from_truecaller(Truecaller_app,"+69839882589")

