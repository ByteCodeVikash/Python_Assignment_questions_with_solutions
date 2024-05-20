"""
2. Write a python script to create a user account class with 2 instance
variables (userid and balance). Create 3 user objects and add all the users 
using operator overloading.

"""

class User_account:
    def __init__(self,userid,balance):
        self.userid=userid
        self.balance=balance

    def __add__(self,other):
        return User_account(self.userid + "&" + other.userid,self.balance + other.balance)
    

    def __repr__(self):
        return f'User_account(userid="{self.userid}", balance={self.balance})'




obj1=User_account("user1",100)
obj2=User_account("user2",200)
obj3=User_account("user3",300)

combined_user=obj1+obj2+obj3

print(combined_user)