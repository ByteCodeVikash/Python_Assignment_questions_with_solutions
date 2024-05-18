"""
7. Write a python program to create a Laptop class with 4 attributes
(brand, ram, cpu,hdd) and 2 methods (showConfig() to print the
values, __init__() to initialize the values).

"""

class Laptop:

    def __init__(self,brand,ram,cpu,hdd):
        self.brand=brand
        self.ram=ram
        self.cpu=cpu
        self.hdd=hdd

    def showConfig(self):
        print(self.brand)
        print(self.ram)
        print(self.cpu)
        print(self.hdd) 

obj=Laptop("hp","24 gb","i9","harddisk")

obj.showConfig()