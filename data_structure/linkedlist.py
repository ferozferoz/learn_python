class LinkedList:

    def __init__(self, data):
        self.data = data
        self.next = None

    def add(self, new_data):

        if self.next is None:
            linked_list = LinkedList(new_data)
            self.next = linked_list
        else:
            self.next.add(new_data)


    def remove(self, data, prev=None):

        if self is None:
            print("list is empty")

        else:

            if self.data == data:
                if prev is None:

                    next_node = self.next
                    if next_node is not None:
                        self.data = next_node.data
                        self.next = next_node.next
                    else:
                        self.data = None
                        self.next = None
                else:
                    prev.next = self.next
            else:
                self.next.remove(data, self)

    def print_list(self):
        if self.next is None:
            print(self.data)
        else:
            print(self.data)
            self.next.print_list()


if __name__ == "__main__":
    lst = LinkedList(9)
    lst.add(10)
    lst.add(11)
    lst.add(12)
    lst.remove(12)
    lst.remove(11)
    lst.remove(9)
    lst.remove(10)
    lst.print_list()