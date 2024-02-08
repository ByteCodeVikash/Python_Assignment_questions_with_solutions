"""
9. Write a python script to check whether a given year is
a. Non century leap year
b. Century leap year
c. Non century non leap year
d. Century non leap year

"""

year = int(input("Enter a year: "))

match year:
    case yr if (yr % 4 == 0 and yr % 100 != 0) or yr % 400 == 0:
        if yr % 100 == 0:
            print(f"{yr} is a century leap year.")
        else:
            print(f"{yr} is a non-century leap year.")
    case yr if yr % 100 == 0:
        print(f"{yr} is a century non-leap year.")
    case _:
        print(f"{year} is a non-century non-leap year.")
