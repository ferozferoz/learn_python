# in this example we will design a decorator that will wrap around any function and do desired action
# - decorator is function that takes function as an input and returns a new function as output
# decorator is defined seperately and it needs to call upon any function with @decorator construct
import time
from functools import wraps

def timethis(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result
    return wrapper


@timethis
def countdown(N):
    while (N > 0):
        N -=1
    print("countdown done")

if __name__=='__main__':
    countdown(1000000)


