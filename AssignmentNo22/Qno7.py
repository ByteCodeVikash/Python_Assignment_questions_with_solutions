#7. Write a recursive python function to calculate sum of the digits of a given number

def digit(n):
    if n==0:
        return 0
    else:
        return (n%10)+digit(n//10)
    


n=int(input("Enter a number: "))
print(digit(n))