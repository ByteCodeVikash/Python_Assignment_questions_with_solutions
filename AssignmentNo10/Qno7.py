#7. Write a python script to print first N even natural numbers in reverse order using for loop and range

i=10
n=1
for x in range(i,n-1,-1):
    if x%2==0:
        print(x)