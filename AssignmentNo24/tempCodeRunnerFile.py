"""
8. WRT 7th Question, create 3 Laptop objects and add them to the list 
in the sorted order based on the ram size

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

laptop1=Laptop("HP","8GB","i3","harddisk")
laptop2=Laptop("lenovo","16GB","i5","512 ssd")
laptop3=Laptop("dell","64 GB","i5","1 tb HHD")

laptops=[laptop1,laptop2,laptop3]

sorted_laptop=sorted(laptops,key=lambda x: int(x.ram.split()[0]))


for laptop in sorted_laptop:
    laptop.showConfig()
    print()