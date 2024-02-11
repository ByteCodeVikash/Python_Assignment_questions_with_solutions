#7. Write a Python script to remove all non int values from a list.

ls=[3,4,"vikash",3.5]

for i in range(len(ls)-1,-1,-1):
    if not isinstance(ls[i],int):
        ls.pop(i)
print(ls)        