#10. Write a recursive python function to find the Nth term of the Fibonacci series


def fib(n):
    if n<=0:
        return "input should be postive integer"
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
    
n=int(input("Enter a number here: "))
print(fib(n))    