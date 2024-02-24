#7. Write a recursive python function to print squares of first N natural numbers


def print_sqr(n):
    if n>0:
        print_sqr(n-1)
        print(n**2)


n=int(input("Enter a number here: ")) 
print_sqr(n)       
