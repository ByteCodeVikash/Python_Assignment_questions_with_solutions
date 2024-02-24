#3. Write a recursive python function to print first N odd natural numbers

def odd_fuc(n,count=1):
    if n>0:
        print(count)
        odd_fuc(n-1,count+2)
    

n=int(input("Enter a number here: "))
odd_fuc(n)        