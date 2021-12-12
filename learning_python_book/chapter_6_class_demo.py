# this example demonstrates inheritance.
# How the childclass can be created by passing parent classs in the constructor


class FirstClass:
    data=None
    key_value = None

    def __init__(self,data=None):
        if data:
            self.data = data  # default value zero

    def set_data(self, value):
        self.data = value

    def display(self):
        print(self.data)

    @classmethod
    def main(cls,key_value):

        instance = cls(key_value)
        print("key value = '{}'".format(instance.data))


class SecondClass(FirstClass):

    def __init__(self,key_value):
        self.data = key_value

    def display(self): # Changes display
        print("Current value = '{}'".format(self.data))


if __name__== "__main__":

    class3 = SecondClass(3)
    class3.set_data(4)
    FirstClass.main(4)
