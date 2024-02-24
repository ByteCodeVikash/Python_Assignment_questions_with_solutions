#9. Write a recursive python function to print first N multiples of a given number



def multiples(n,m,count=1):
    if n>0:
        print(m*count)
        multiples(n-1,m,count+1)


n=int(input("Enter a first number here: "))
m=int(input("Enter a second number here: "))
multiples(n,m)        