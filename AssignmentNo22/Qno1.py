#1. Write a recursive python function to calculate sum of first N natural numbers

def add(n):
    if n<=0:
        return 0
    else:
        return n+add(n-1)
  

n=int(input("Enter a number here: "))
r=add(n)
print(r)