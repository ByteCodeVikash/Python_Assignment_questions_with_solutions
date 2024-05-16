#8. Create an endless iterator using generator method to produce Prime numbers

def is_prime(num):
    if num<=1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True

def prime_gen():
    num=2
    while True:
        if is_prime(num):
            yield num
        num+=1

prime_gen_no=prime_gen()

for _ in range(10):
    print(next(prime_gen_no))