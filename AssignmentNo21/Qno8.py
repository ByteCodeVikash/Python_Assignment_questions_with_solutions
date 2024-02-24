#8. Write a recursive python function to print cubes of first N natural numbers


def print_cubes(n):
    if n>0:
        print_cubes(n-1)
        print(n**3)

n=int(input("Enter a number here: "))
print_cubes(n)        