"""6. Write a python script which takes a three digit number from the user and
 displays
only its middle digit"""


num=int(input("Enter a there digit number here: "))

digit=(num//10)%10

print("The middle digit is",digit)