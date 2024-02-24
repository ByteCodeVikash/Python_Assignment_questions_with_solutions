"""
4. Write a recursive python function to calculate sum of squares of first N natural
numbers

"""
def sum_sqr(n):
    if n<=0:
        return 0
    else:
        return (n**2)+sum_sqr(n-1)
    
n=int(input("Enter a number here: "))
print(sum_sqr(n))    