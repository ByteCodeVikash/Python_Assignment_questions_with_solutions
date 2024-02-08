"""10. Write a python script to display the current date and time. 
First create variables to
store date and time, then display date and time in proper format 
(like: 13-8-2022 and
9:00 PM)"""



from datetime import datetime
current_datetime=datetime.now()
date=current_datetime.strftime("%d-%m-%y")
time=current_datetime.strftime("%I-%m-%p")

print("date",date)
print("time",time)