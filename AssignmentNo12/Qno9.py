#9. Write a python script to calculate LCM of two numbers using loop

num1=int(input("Enter a first number here: "))
num2=int(input("Enter a second number here: "))

max_num=max(num1,num2)

lcm=max_num
while True:
    if lcm%num1==0 and lcm%num2==0:
        print("LCM of",num1,"and",num2,"is",lcm)
        break
    lcm+=max_num