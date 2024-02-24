#3. Write a recursive python function to calculate sum of first N even natural numbers

def add_even(n):
    if n<=0:
        return 0
    else:
        return(2*n)+add_even(n-1)
    
n=int(input("Enter a number here: "))
print(add_even(n))
