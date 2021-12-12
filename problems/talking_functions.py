import time



def function1(counter):
    print("hello function 2 ")
    time.sleep(10)
    counter += 1
    print("counter value"+ str(counter))
    function2()

def function2(counter):

    print("hello function 1")
    time.sleep(10)
    counter += 1
    print("counter value"+ str(counter))
    function2(counter)


if __name__== "__main__":
    counter=1
    function1(counter)