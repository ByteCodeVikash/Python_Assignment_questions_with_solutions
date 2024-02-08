#8. Write a python script to calculate simple interest

principal=int(input("Enter a principal here: "))
rate=int(input("Enter a rate here: "))
time=int(input("Enter a time here: "))

simple_interest=(principal*rate*time/100)

print("Simple interest",simple_interest)