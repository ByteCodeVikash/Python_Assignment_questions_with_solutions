"""
10. Define a function which calculates HCF of two numbers. Define and apply a
decorator to check whether two given numbers are co-prime or not.

"""

def check_coprime(func):
    def wrapper(a,b):
        for i in range(2,min(a,b)+1):
            if a%i==0 and b%i==0:
                print("The given number are not co-prime.")
                return
        return func(a,b)
    return wrapper

@check_coprime
def cal_hcf(a,b):
    while b:
        a,b=b,a%b
    print("HCF of the given number: ",a)

cal_hcf(35,48)
cal_hcf(15,25)    
