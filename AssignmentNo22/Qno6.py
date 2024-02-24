#6. Write a recursive python function to calculate the factorial of a number.

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
    

n=int(input("Enter a number here"))
print(factorial(n))