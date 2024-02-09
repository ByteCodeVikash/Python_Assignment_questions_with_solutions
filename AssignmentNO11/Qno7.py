#7. Write a python script to count digits in a given number using loop

number = int(input("Enter a number: "))
count = 0

# Handling negative numbers
if number < 0:
    number *= -1

# Counting digits using a loop
while number > 0:
    count += 1
    number //= 10

print("Number of digits:", count)
      