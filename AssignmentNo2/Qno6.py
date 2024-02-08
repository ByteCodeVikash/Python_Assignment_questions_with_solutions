#6. Write a python script to print all the keywords

import keyword

kwlist=keyword.kwlist

for a in kwlist:
    print(a,end=',')