class heap:
    def __init__(self):
        self.counter = 0
        self.list_append = [0]

    def shift_up(self,index):
        while (index //2 > 0 ):
            if (self.list_append[index] < self.list_append[index //2] ):
                # swap the positions in python
                self.list_append[index] , self.list_append[index // 2] = self.list_append[index //2] , self.list_append[index]

            index = index //2

    def insert(self,element):
        self.counter +=1
        self.list_append.append(element)
        self.shift_up(self.counter)


if __name__== "__main__":
    print(str(0 // 2))
    print (str(1//2))
    print(str(2 // 2))
    print(str(3 // 2))
    print(str(4 // 2))

    heap = heap()
    heap.insert(4)
    heap.insert(6)
    heap.insert(3)
    heap.insert(1)
    heap.insert(7)

    print(heap.list_append)