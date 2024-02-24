#2. Write a recursive python function to print first N natural numbers in reverse order

def fuc_n(n):
    if n>0:
        print(n)
        fuc_n(n-1)
        
    

n=int(input("Enter a number here: "))
fuc_n(n)    