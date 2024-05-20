"""
3. Write a python script to create a to print the above user account object
using operator overloading (hint __str__ method).

"""

class UserAccount:
    def __init__(self,userid,balance):
        self.userid=userid
        self.balance=balance

    def __add__(self,other):
        return UserAccount(self.userid + "&" + other.userid,self.balance+other.balance)

    def __repr__(self):
        return f'UserAccount(userid="{self.userid}",balance={self.balance})'

    def __str__(self):
        return f'UserAccount:{self.userid}, Balance:{self.balance}'

user1=UserAccount("user1",100)
user2=UserAccount("user2",200)
user3=UserAccount("user3",300)

compine_user=user1+user2+user3

print(compine_user)