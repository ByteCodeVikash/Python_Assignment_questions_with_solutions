#5. Write a recursive python function to calculate sum of cubes of first N natural numbers


def sum_cubes(n):
    if n<=0:
        return 0
    else:
        return(n**3)+sum_cubes(n-1)
    

n=int(input("Enter a number here: "))
print(sum_cubes(n))    