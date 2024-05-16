#1. Use iter and next method to access all the elements of a given set using while loop

my_set={1,2,3,4,5}
my_itertor=iter(my_set)
while True:
    try:
        element=next(my_itertor)
        print(element)
    except StopIteration:
        break
        
