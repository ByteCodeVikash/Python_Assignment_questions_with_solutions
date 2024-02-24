#2. Write a recursive python function to calculate sum of first N odd natural numbers


def add_odd(n):
    if n<=0:
        return 0
    else:
        return(2*n-1)+add_odd(n-1)

n=int(input("Enter a number here: "))
r=add_odd(n)
print(r)