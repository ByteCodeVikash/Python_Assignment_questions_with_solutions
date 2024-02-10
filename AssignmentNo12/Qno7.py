"""
7. Write a python script to check whether a given pair of numbers are co-Prime
numbers or not.

"""

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

gcd = 1
for i in range(2, min(number1, number2) + 1):
    if number1 % i == 0 and number2 % i == 0:
        gcd = i
        break

if gcd == 1:
    print(number1, "and", number2, "are coprime numbers")
else:
    print(number1, "and", number2, "are not coprime numbers")
