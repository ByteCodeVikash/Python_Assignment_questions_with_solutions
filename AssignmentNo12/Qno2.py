#2. Write a python script to check whether a given number is Prime or not using loop

num=int(input("Enter a number here: "))

is_prime=True

if num<=1:
    is_prime=False

else:
    for i in range(2,num):
        if num%i==0:
            is_prime=False
            break

if is_prime:
    print(num,"is prime number")

else:
    print(num,"is not prime number")
       