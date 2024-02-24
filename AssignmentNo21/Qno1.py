#1. Write a recursive python function to print first N natural numbers

def fuc_rec(n):
    if n>0:
        fuc_rec(n-1)
        print(n)  

n=int(input("Enter a number here: "))
fuc_rec(n)
