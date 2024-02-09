#8. Write a python script to calculate sum of digits of a given number using loop

number = int(input("Enter a number: "))
sum_of_digits = 0

# Handling negative numbers
if number < 0:
    number *= -1

# Calculating sum of digits using a loop
while number > 0:
    digit = number % 10
    sum_of_digits += digit
    number //= 10

print("Sum of digits:", sum_of_digits)
