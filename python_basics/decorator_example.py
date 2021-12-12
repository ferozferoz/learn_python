from datetime import datetime
def say_hello():
    print("Hello")
"""decorator can help to manage running of function"""

def check_time_of_function(f):
    def wrapper():
        if datetime.now().hour > 7 and datetime.now().hour < 22:
            print("its day so function will run")
            f()
        else:
            print("Shh.. its nighttime")

    return wrapper

f1 =check_time_of_function(say_hello)
f1()