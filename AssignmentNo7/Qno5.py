"""5. Write a program which takes a number from user. Print Vikash if the 
number
is even, print Prateek  if the number is negative odd number and print Aditya
 if number is positive odd number.
"""
num=int(input("Enter a number here: "))

match num:
    case num if num%2==0:
        print("Vikash")
    case num if num%2!=0 and num<0:
        print("Prateek ")
    case num if num%2!=0 and num>0:
        print("Aditya")       

