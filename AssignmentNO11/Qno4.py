#4. Write a python script to calculate sum of first N odd natural numbers using loop

n=int(input("Enter a postive number here: "))

odd=0

for i in range(1,n+1):
    if i%2!=0:
        odd+=i

print(odd)       