#6. Create a generator to produce first n prime numbers


def prime_no(num):
    if num<=1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True

def prime_number(n):
    count=0
    num=2
    while count<n:
        if prime_no(num):
            yield num
            count+=1
        num+=1

n=10
prime_gen=prime_number(n)

for _ in range(n):
    print(next(prime_gen))


 