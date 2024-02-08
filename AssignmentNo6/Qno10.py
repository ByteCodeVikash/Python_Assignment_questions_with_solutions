"""10. Write a python script to print greater among three numbers.
 Print number only once
even if the numbers are the same."""

num1=int(input("Enter a first number here: "))
num2=int(input("Enter a second number here: "))
num3=int(input("Enter a third number here: "))

if num1>num2 and num1>num3:
    print(num1,"is greater number")
elif num2>num1 and num2>num3:
    print(num2,"is greater number")
else:
    print(num3,"is a greater number")        