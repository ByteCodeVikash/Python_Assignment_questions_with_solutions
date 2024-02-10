#1. Write a python script to reverse a number using loop

num=12345

reverse=0

while num>0:
    digit=num%10
    reverse=(reverse*10)+digit
    num=num//10

print("original num",num)
print("reverse",reverse)    