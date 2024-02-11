#2. Write a Python script to create a list of first N odd natural numbers.

n = 10
odd_numbers = []

i = 1
while len(odd_numbers) < n:
    if i % 2 != 0:  # Checking if the number is odd
        odd_numbers.append(i)
    i += 1

print(odd_numbers)


    