#2. Write a python script to calculate sum of squares of first N natural numbers using loop

n=int(input("Enter a postive number: "))

squares=0

for i in range(1,n+1):
    squares+=i**2

print("The squares of first",n,"natual number",squares)    