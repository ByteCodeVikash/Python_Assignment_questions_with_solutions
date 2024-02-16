"""
2. Write a python program to create a function that takes a number as a parameter and
checks if the number is prime or not

"""
def is_prime(num):

    if num>1:
        for i in range(2,num):
            if num%i==0:
                print(num,"is prime number")
                break
        else:
             print(num,"is prime number")
    else:
        print(num,"is not prime number")        
num=int(input("Enter a number here: "))

is_prime(num)