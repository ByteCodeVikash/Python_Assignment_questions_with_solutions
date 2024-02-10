#5. Write a python script to find next prime number of a given number using loop

num = int(input("Enter a number: "))
next_prime = num + 1

while True:
    is_prime = True
    for i in range(2, next_prime):
        if next_prime % i == 0:
            is_prime = False
            break
    if is_prime:
        print("The next prime number after", num, "is:", next_prime)
        break
    next_prime += 1

