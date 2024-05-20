#6. Write a python script to create 5 threads to fill a list with random numbers till 100

import threading

import random


def fill_list_with_random_number(lst):
    for _ in range(100):
        lst.append(random.randint(1,100))

random_number_list=[]

threads=[]

for _ in range(5):
    thread=threading.Thread(target=fill_list_with_random_number,args=(random_number_list,))
    threads.append(thread)
    thread.start()


for thread in threads:
    thread.join()


print("Random number list: ",random_number_list)        