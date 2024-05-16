#4. Create a generator to produce squares of first N natural numbers

def sqr_gen_no(n):
    count=0
    num=1
    while count<n:
        yield num**2
        num+=1
        count+=1

n=10
result=sqr_gen_no(n)

for _ in range(n):
    print(next(result))