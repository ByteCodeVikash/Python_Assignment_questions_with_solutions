#9. Write a recursive python function to print octal of a given decimal number


def octal(n):
    if n==0:
        print(0,end='')
        return
    elif n>0:
        octal(n//8)
        print(n%8,end='')

n=int(input("Enter a number here: "))
octal(n)            