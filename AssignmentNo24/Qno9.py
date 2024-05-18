"""
9. Write a python program to create a School class and 3 instance variables
and 1 class variable.

"""

class School:
    #class variable
    total_students=0

    #instance variable
    def __init__(self,name,loaction,year):
        self.name=name
        self.loaction=loaction
        self.year=year

    #increment
        School.total_students+=1

School1=School("central public school","zamanaia",1997)
School2=School("st.marry school","kasba",1990)
School3=School("delhi public school","delhi",1977)

print("total students all school",School.total_students)

