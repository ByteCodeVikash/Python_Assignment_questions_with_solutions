#6. Write a python script to check whether a given number is a three digit number or not.

number = input("Enter a three-digit number: ")

if number.isdigit() and len(number) == 3:
    print("The number is a three-digit number.")
else:
    print("The number is not a three-digit number.")
 
