#3. Write a python script to calculate sum of cubes of first N natural numbers using loop

n=int(input("Enter a positive number here: "))

cube=0

for i in range(1,n+1):
    cube+=i**3

print("The cubes of first",n,"natural number",cube)    