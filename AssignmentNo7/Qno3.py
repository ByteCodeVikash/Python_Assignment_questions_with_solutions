"""3. Write a menu driven program with the following options:
a. Check whether a given set of three numbers are lengths of an isosceles
triangle or not
b. Check whether a given set of three numbers are lengths of sides of a right
angled triangle or not
c. Check whether a given set of three numbers are equilateral triangle or not
d. Exit.
"""

print("Menu")
print("1.isosceles")
print("2.right angled Triangle")
print("3.equilateral triangle")
print("4.exit")

choice=int(input("Enter your choice 1 to 4: "))

match choice:
    case 1:

        side1=int(input("Enter a side 1: "))
        side2=int(input("Enter a side 2: "))
        side3=int(input("Enter a side 3: "))

        if (side1==side2) or side1==side3 or side2==side3:
            print("These lenght for isosceles triangl")
        else:
            ("these length not for isosceles triangle") 


    case 2:
        side1=int(input("Enter a side1: "))
        side2=int(input("Enter a side2: "))
        side3=int(input("Enter a side3: "))

        sides=[side1,side2,side3]

        sides.sort()

        if sides[0]**2+sides[1]**2==sides[2]**2:
            print("These length of right angle triangle")
        else:
            print("These length do not right angle triangle triangle")

    case 3:
        side1=int(input("Enter a side1: "))
        side2=int(input("Enter a side2: "))
        side3=int(input("Enter a side3: ")) 


        if side1==side2==side3:
            print("These lengths form an equilateral triangle. ") 
        else:
            print("These lengths not form an equilateral triangle.") 

    

    case _:
        print("invild input")                      