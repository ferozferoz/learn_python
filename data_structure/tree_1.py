class Tree:

    def __init__(self,data):
        self.data = data
        self.left_node=None
        self.right_node=None

    def add_node(self, newdata):

        tree = Tree(newdata)
        if self.data > newdata:
            if self.left_node is None:
                self.left_node = tree
            else:
                self.left_node.add_node(newdata)
        else:
            if self.right_node is None:
                self.right_node = tree
            else:
                self.right_node.add_node(newdata)

    def traverse(self,pointer=None):
        if pointer.left_node is not None:
            pointer.traverse(pointer.left_node)
        print(pointer.data)
        if pointer.right_node is not None:
            pointer.traverse(pointer.right_node)


    def sum_nodes(self,sum=None):
        if sum is None:
            sum=0

        if self.left_node is not None:
            sum = self.left_node.sum_nodes(sum)

        sum += self.data
        if self.right_node is not None:
            sum = self.right_node.sum_nodes(sum)

        return sum

    def sum_parent_node_given_child(self,search_data,sum=None):
        if sum is None:
            sum=0
        else:
            if self.data < search_data:
                sum=sum+self.data
                self.right_node.sum_parent_node_given_child(search_data,sum)
            elif self.data > search_data:
                sum = sum + self.data
                self.left_node.sum_parent_node_given_child(search_data, sum)
            else:
                sum = sum + self.data

        print(sum)

if __name__ == "__main__":

    tree = Tree(10)
    tree.add_node(11)
    tree.add_node(9)
    tree.add_node(8)
    tree.add_node(12)

    tree.traverse(tree)
    tree.sum_parent_node_given_child(10)
