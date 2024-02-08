"""12. Write a python script to accept one complex number from the user
 and display the
greater number between real part and imaginary part"""

# Accept a complex number from the user
complex_number = complex(input("Enter a complex number: "))

# Get the real and imaginary parts
real_part = complex_number.real
imaginary_part = complex_number.imag

# Compare the real and imaginary parts
if real_part > imaginary_part:
    print("The greater number is the real part:", real_part)
elif real_part < imaginary_part:
    print("The greater number is the imaginary part:", imaginary_part)
else:
    print("The real and imaginary parts are equal:", real_part)
