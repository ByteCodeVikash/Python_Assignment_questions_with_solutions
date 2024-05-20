#9. Write a python script to join 2 threads after printing completing the first Question


import threading
import time

def execute_first_question():
    print("Executing first question..")
    time.sleep(5)
    print("Frist question completed!")

def execute_second_task():
    print("Executing second task...") 
    time.sleep(3)
    print("Second Task completed")

thread1=threading.Thread(target=execute_first_question)
thread2=threading.Thread(target=execute_second_task)

thread1.start()
thread2.start()

thread1.join()
print("Thread 1 joined")

thread2.join()
print("Thread 2 joined")


print("Both threads have completed their excution!")