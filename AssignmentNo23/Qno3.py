#3. Create a generator to produce first n even natural numbers

def even_no(n):
    count=0
    num=2
    while count<n:
        yield num
        count+=1
        num+=2

n=(10)
even_gen=even_no(n)
for _ in range(n):
    print(next(even_gen))      