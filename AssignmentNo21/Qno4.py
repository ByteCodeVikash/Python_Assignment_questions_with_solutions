#4. Write a recursive python function to print first N odd natural numbers in reverse order


def reverse_odd(n,count=0):
    if  n>0:
        
        reverse_odd(n-1,count+2)
        print(count)



n=int(input("Enter a number here: "))
reverse_odd(n)    