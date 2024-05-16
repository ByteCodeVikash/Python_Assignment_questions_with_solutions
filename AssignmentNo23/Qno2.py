#2. Create a generator to produce first n odd natural numbers

def odd_no(n):
    count=0
    num=1
    while count<n:
        yield num
        num+=2
        count+=1

n=5
odd_gen=odd_no(n)

for _ in range(n):
    print(next(odd_gen))
