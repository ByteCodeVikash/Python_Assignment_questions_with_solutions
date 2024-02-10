#10. Write a python script to calculate HCF of two numbers using loop

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Find the minimum of the two numbers
min_num = min(num1, num2)

# Initialize HCF as 1
hcf = 1

for i in range(1, min_num + 1):
    if num1 % i == 0 and num2 % i == 0:
        hcf = i

print("HCF of", num1, "and", num2, "is:", hcf)
       