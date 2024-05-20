#5. Write a python script to create 2 threads to add all the values from 1 to 100

import threading

def calculate_sum(start,end,result):
    total=sum(range(start,end+1))
    result.append(total)


results=[]

thread1=threading.Thread(target=calculate_sum,args=(1,50,results))
thread2=threading.Thread(target=calculate_sum,args=(51,100,results))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

total_sum=sum(results)

print(total_sum)

