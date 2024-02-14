"""
7. Write a python program to create three dictionaries, then create one dictionary that
will contain the other three dictionaries.

"""

dict1={'a':1,'b':2,'c':3}
dict2={1:'a',2:'b',3:'c'}
dict3={'A':1,'B':2,'C':3}

combine_dict={'dict1':dict1,'dict2':dict2,'dict3':dict3}

print(combine_dict)