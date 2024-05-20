"""10. Write a python script to check whether a given number is prime or armstrong number
using 2 different threads."""

import threading
import math

def is_prime(number):
    if number <=1:
        return False
    elif number <=3:
        return True
    elif number %2 ==0 or number % 3==0:
        return False
    i=5

    while i* i <=number:
        if number % i==0 or number % (i + 2)==0:
            return False
        i+=6
    return True


def is_armstrong(number):
    num_str=str(number)
    num_digits=len(num_str)
    sum_of_digits=sum(int(digit)**num_digits for digit in num_str)
    return sum_of_digits==number


def check_prime_and_armstrong(number):
    prime_thread=threading.Thread(target=check_prime,args=(number,))
    armstrong_thread=threading.Thread(target=check_armstrong,args=(number,))

    prime_thread.start()
    armstrong_thread.start()

    prime_thread.join()
    armstrong_thread.join()

def check_prime(number):
    if is_prime(number):
        print(number,"is a prime number") 
    else:
        print(number,"is not a prime number")

def check_armstrong(number):
    if is_armstrong(number):
        print(number,"is an Armstrong number")

    else:
        print(number,"is not a Armstrong number")

if __name__=="__main__":
    number=int(input("Enter a number here: "))
    check_prime_and_armstrong(number)                   
