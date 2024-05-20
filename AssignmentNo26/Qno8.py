#8. Write a python script to change the name of the Thread.


import threading
import time

def print_current_time():
    while True:
        current_time=time.strftime("%H:%M:%S",time.localtime())
        print(threading.current_thread().getName(),"Current Time: "+current_time)
        time.sleep(1)

thread1=threading.Thread(target=print_current_time)

thread1.start()

thread1.setName("Time Printing Thread")