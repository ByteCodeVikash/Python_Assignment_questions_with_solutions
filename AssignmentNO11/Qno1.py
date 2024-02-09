#1. Write a python script to calculate sum of first N natural numbers using loop

n=int(input("Enter a positive number: "))

sum=0

for i in range(1,n+1):
    sum+=i

print("The sum of first",n,"natural number is",sum)    