#6. Write a python script to calculate factorial of a given number using loop

n=int(input("Enter a postive number here: "))

fact=1

for i in range(1,n+1):
    fact*=i

print(fact)    