#7. Write a python program to access a function inside a function.

def outer_fuc():
    print("This is outer function")

    def inner_fuc():
        print("This is inner function")

    inner_fuc()    



outer_fuc()
