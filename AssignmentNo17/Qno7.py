"""
7. Write a python program to remove last item of the given set
thisset = {"Python", "Django", "JavaScript", “SQL”}

"""

thisset={"Python","Django","JavaScript","Sql"}

ls=list(thisset)

ls.pop()

thisset=set(ls)

print(thisset)