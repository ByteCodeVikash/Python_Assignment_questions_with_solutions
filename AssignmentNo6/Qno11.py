"""11. Write a python script to take the month value in numeric format and
 display the
number of days in it.
"""

x=int(input("Enter a month value in numeric format: "))

match x:
    case 1:
        print("31")
    case 2:
        print("28,29") 
    case 3:
        print("31")
    case 4:
        print("30")
    case 5:
        print("31")
    case 6:
        print("30")
    case 7:
        print("31")
    case 8:
        print("31")
    case 9:
        print("30")
    case 10:
        print("31")
    case 11:
        print("30")
    case 12:
        print("31")                                           