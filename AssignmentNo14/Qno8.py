"""
8. Write a Python script to print distinct elements along with their frequencies of
occurrence in the list.

"""

from collections  import Counter

mylist=[1,2,3,1,2,3,6,9,0,4]

element_frq=Counter(mylist)

for element,frq in element_frq.items():
    print("Element",element,"Frequencis",frq)

