#6. Write a recursive python function to print first N even natural numbers in reverse order.


def even_revrse(n,count=2):
    if n>0:
        even_revrse(n-1,count+2)
        print(count)

n=int(input("Enter a number here: "))
even_revrse(n)        
