#5. Write a python script to calculate sum of first N even natural numbers using loop

n=int(input("Enter a postive number here: "))

even=0

for i in range(1,n+1):
    if i%2==0:
        even+=1

print(even)        