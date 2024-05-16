#5. Create a generator to produce first n terms of Fibonacci series

def feb_no(n):
    a,b=0,1
    count=0
    while count<n:
        yield a
        a,b=b,a+b
        count+=1


n=10
result=feb_no(n)

for _ in range(n):
    print(next(result))