#5. Write a recursive python function to print first N even natural numbers.

def even_fuc(n,count=2):
    if n>0:
        print(count)
        even_fuc(n-1,count+2)


n=int(input("Enter a number here: "))
even_fuc(n)