#10. Write a recursive python function to print a number in reverse order

def reverse_digits(n):
    str_n = str(n)
    if len(str_n) == 1:  
        print(str_n, end='')
    else:
        
        print(str_n[-1], end='')
        reverse_digits(int(str_n[:-1]))
 
n = int(input("Enter a number here: "))
reverse_digits(n)

