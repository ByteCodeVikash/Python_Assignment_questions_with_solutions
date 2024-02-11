#3. Write a Python script to create a list of first N even natural numbers.

n=10
even_no=[]

i=1

while len(even_no)<n:
    if i%2==0:
        even_no.append(i)
    i+=1
print(even_no)        