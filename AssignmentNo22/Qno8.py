#8. Write a recursive python function to print binary of a given decimal number


def bin_fuc(n):
    if n==0:
        print(0,end='')
    elif n>0:
            bin_fuc(n//2)
            print(n%2,end='')

n=int(input("Enter a number here: "))
bin_fuc(n)                