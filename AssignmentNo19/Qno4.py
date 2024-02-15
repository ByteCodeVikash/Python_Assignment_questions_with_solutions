#4. Write a python program to create a function which expects kwargs arguments.


def fuc(**kwargs):
    for key,value in kwargs.items():
        print(key,value)

fuc(name="vikash",age=24,city="Delhi")        