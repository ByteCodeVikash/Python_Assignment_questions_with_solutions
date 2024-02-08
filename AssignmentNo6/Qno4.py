"""4. Write a python script to print greater between two numbers. 
Print number only once
even if the numbers are the same.
"""

num1 =int(input("Enter a first number here: "))
num2=int(input("Enter a second number here: "))

if num1>num2:
    print(num1,"is the greater than second number")
elif num2>num1:
    print(num2,"is greater than first number ") 
else:
    print("the number are the same")       