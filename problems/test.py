class Example:
    num=0
    def __init__(self):
        Example.num=0

    def met(cls):
        Example.num =Example.num+1

    def example(self):
        return self.__test()

    def __test(self):
        return 'hello'

if __name__ == "__main__":
    #ex = Example()
    #print(ex.example())
    #print(ex.__test())

    #a = [1,2,2,4]
    #print(a[-1])
    #print((0+2)//2)

    for x in reversed(range(1,4)):
        print(x)
    #print(Example.test())
    #ex.met()
    #print(ex.num)
    #print(Example.example())