#5. Write a python program to create a function to find the Min of three numbers.


def min_func(num1, num2, num3):
    return min(num1, num2, num3)

print("Enter three numbers:")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

minimum = min_func(num1, num2, num3)
print("Minimum of the three numbers is:", minimum)
