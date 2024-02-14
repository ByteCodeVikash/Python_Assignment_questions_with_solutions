#9. Write a python program to merge two python dictionaries into one dictionary.


#using update method

dict1={'a':1,'b':2,'c':3}
dict2={11:'A',22:'B',33:'C'}

dict1.update(dict2)

print(dict1)

#using unpacking method

dict1={'a':1,'b':2,'c':3}
dict2={11:'A',22:'B',33:'C'}

combine_dict={**dict1,**dict2}

print(combine_dict)
