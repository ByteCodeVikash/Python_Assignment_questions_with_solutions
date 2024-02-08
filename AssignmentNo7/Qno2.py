"""2. Write a menu driven program to perform following operations
 - Addition, Subtraction,
Multiplication, Division
"""

print("Menu")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

choice=int(input("Enter your choice 1 to 5: "))

num1=int(input("Enter a first number here: "))
num2=int(input("Enter a second number here: "))

match choice:
        case 1:
            results=num1+num2
            print("results",results)
        case 2:
            results=num1-num2
            print("results",results)
        case 3:
            results=num1*num2
            print("results",results)
        case 4:
            results=num1/num2
            print("results",results)            
    