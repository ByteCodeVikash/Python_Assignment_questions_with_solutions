"""
10. Write a python script to print the octal equivalent of a given decimal number.
 (do not
use oct() method) using loop only
"""

dec=int(input("Enter a decimal number here: "))

oct=''

if dec<0:
    oct="0"

else:
    while dec>0:
        reminder=dec%8
        oct=str(reminder)+oct
        dec//=8

print("octal equivalent",oct)            