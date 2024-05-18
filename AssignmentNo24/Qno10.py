"""
10. Define a class Employee with instance object variables 
empid, name, salary. Write __init__() method in the class to
initialize instance object variables. Also define
instance methods to input fields and display field values

"""

class Employee:
    def __init__(self,empid,name,salary):
        self.empid=empid
        self.name=name
        self.salary=salary

    def inputfield(self):
        self.empid=input("Enter your empid here: ")
        self.name=input("Enter your name here: ")
        self.salary=input("Enter your salary here: ") 

    def inputdisplay(self):
        print(self.empid)
        print(self.name)
        print(self.salary)

obej=Employee(101,"Vikash",50000)

obej.inputdisplay()