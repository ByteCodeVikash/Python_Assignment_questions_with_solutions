"""
7. Write a python script to create a clock where 1st thread will print the
current time every second and 2nd will print “1 Minute Completed” after every
1 minute.

"""

import threading
import time

def print_current_time():
    while True:
        current_time=time.strftime("%H:%M:%S",time.localtime())
        print("Current Time: ",current_time)
        time.sleep(1)

def print_minute_completed():
    while True:
        time.sleep(60)
        print("1 minute completed")


thread1=threading.Thread(target=print_current_time)
thread2=threading.Thread(target=print_minute_completed)

thread1.start()
thread2.start()

thread1.join()
thread2.join()


