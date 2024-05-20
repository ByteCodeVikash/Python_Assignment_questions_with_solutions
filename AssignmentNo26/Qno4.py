"""
4. Write a python script to create two Threads. First thread will print
all Even numbers and Second thread will print all Odd numbers till 100.

"""
import threading

def print_even():
    for i in range(2,101,2):
        print("even",i)

def print_odd():
    for i in range(1,101,2):
        print("odd",i)


thread1=threading.Thread(target=print_even)
thread2=threading.Thread(target=print_odd)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Done")


        