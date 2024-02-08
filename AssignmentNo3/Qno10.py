"""10. Write a python script to add two numbers 25 (in octal) and 39 (in hexadecimal)
 and
display the result in binary format."""

octal='25'
hexa='39'

binary1=int(octal,8)
binary2=int(hexa,16)

binary=bin(binary1+binary2)

print(binary)