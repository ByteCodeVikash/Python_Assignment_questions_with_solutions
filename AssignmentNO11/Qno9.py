"""
9. Write a python script to print binary equivalent of a given decimal number.
 (do not
use bin() method) using loop
"""

deci_number=int(input("Enter a decimal number here: "))

binary=''

if deci_number==0:
    binary="0"

else:
    while deci_number>0:
        reminder=deci_number%2
        binary=str(reminder)+binary
        deci_number//=2

print("binary equivalent",binary)            
