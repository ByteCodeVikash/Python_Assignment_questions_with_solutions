"""
7. Create an endless iterator using generator method to produce 
terms of Fibonacci series

"""

def feb_no():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b

fib_gen=feb_no()

for _ in range(10):
    print(next(fib_gen))

