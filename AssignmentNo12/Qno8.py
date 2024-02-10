#8. Write a python script to print first N terms of a Fibonacci series using loop


N = int(input("Enter the number of terms: "))

# Initialize the first two terms
a, b = 0, 1
count = 0

# Check if the number of terms is valid
if N <= 0:
    print("Please enter a positive integer")
elif N == 1:
    print("Fibonacci sequence upto", N, ":", a)
else:
    print("Fibonacci sequence:")
    while count < N:
        print(a, end=" ")
        nth = a + b
        # Update values for next iteration
        a = b
        b = nth
        count += 1
