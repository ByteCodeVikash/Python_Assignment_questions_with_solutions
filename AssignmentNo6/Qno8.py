"""8. Write a python script to check whether a given quadratic equation has 
two real &
distinct roots, real & equal roots or imaginary roots
"""

# Coefficients of the quadratic equation
a = float(input("Enter the coefficient of x^2: "))
b = float(input("Enter the coefficient of x: "))
c = float(input("Enter the constant term: "))

# Calculate the discriminant
discriminant = b**2 - 4*a*c

# Check the nature of the roots
if discriminant > 0:
    print("The quadratic equation has two real and distinct roots.")
elif discriminant == 0:
    print("The quadratic equation has real and equal roots.")
else:
    print("The quadratic equation has imaginary roots.")
