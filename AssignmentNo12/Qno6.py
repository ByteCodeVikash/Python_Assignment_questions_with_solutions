#6. Write a python script to print first N prime numbers using loop

n=50

for num in range(2,n):
    for i in range(2,num):
        if num%i==0:
            break
    else:
        print(num,end=',')    