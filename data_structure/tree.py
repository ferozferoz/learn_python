"""implementation of simple tree in python"""

class TreeClass:

    def __init__(self, data):
        self.data = data
        self.left_node = None
        self.right_node = None

    """complexity - the the worst case - you might need to traverse O(n) to insert node"""

    def add_node(self, newdata):
        node = TreeClass(newdata)

        if newdata >= self.data:
            if self.right_node is None:
                self.right_node = node
            else:
                self.right_node.add_node(newdata)
        if newdata < self.data:
            if self.left_node is None:
                self.left_node = node
            else:
                self.left_node.add_node(newdata)

    def add_node_reference(self, node):

        if node.data >= self.data:
            if self.right_node is None:
                self.right_node = node
            else:
                self.right_node.add_node_reference(node)
        if node.data < self.data:
            if self.left_node is None:
                self.left_node = node
            else:
                self.left_node.add_node_reference(node)

    """complexity - the the worst case - you might need to traverse O(n) to traverse and find node"""

    def find_node(self, newdata):
        if newdata > self.data:
            if self.right_node is None:
                print("Node" + str(newdata) + " not found!")
            else:
                self.right_node.find_node(newdata)
        elif newdata < self.data:
            if self.left_node is None:
                print("Node" + str(newdata) + " not found!")
            else:
                self.left_node.find_node(newdata)
        else:
            print("Node" + str(newdata) + " found!")

    def sub_tree(self, newdata):

        if newdata > self.data:
            if self.right_node is None:
                return self
            else:
                return self.right_node.sub_tree(newdata)
        elif newdata < self.data:
            if self.left_node is None:
                return self
            else:
                return self.left_node.sub_tree(newdata)
        else:
            return self

    def find_parent(self, node_value, parent=None):

        if self.data == node_value:
            return parent
        elif node_value > self.data:
            parent = self
            if self.right_node is None:
                return None
            else:
                return self.right_node.find_parent(node_value,parent)
        else:
            parent = self
            if self.left_node is None:
                return None
            else:
                return self.left_node.find_parent(node_value, parent)

    def delete_node(self, node_value):
        parent_node = self.find_parent(node_value)
        if parent_node is None:
            node_to_be_returned = self.right_node
            node_to_be_returned.add_node_reference(self.left_node)
            return node_to_be_returned
        else:
            if parent_node.data > node_value:
                node_to_be_deleted = parent_node.left_node
                parent_node.left_node = node_to_be_deleted.right_node
                parent_node.left_node.add_node_reference(node_to_be_deleted.left_node)
            else:
                node_to_be_deleted = parent_node.right_node
                parent_node.right_node = node_to_be_deleted.right_node
                parent_node.right_node.add_node_reference(node_to_be_deleted.left_node)
            return self

    """binary tree traversal
    1. inorder traversal - left tree is visited first , root and then right subtree
    2. pre order traversal - root is visited first then left subtree and then right subtree 
    3. post order traversal - root is visited last  """

    def inorder_print_tree(self):
        if self.left_node:
            self.left_node.inorder_print_tree()
        print(self.data)
        if self.right_node:
            self.right_node.inorder_print_tree()

    def preorder_print_tree(self):
        print(self.data)
        if self.left_node:
            self.left_node.preorder_print_tree()
        if self.right_node:
            self.right_node.preorder_print_tree()

    def postorder_print_tree(self):
        if self.left_node:
            self.left_node.postorder_print_tree()
        if self.right_node:
            self.right_node.postorder_print_tree()
        print(self.data)


if __name__ == "__main__":
    tree_nd = TreeClass(10)
    tree_nd.add_node(12)
    tree_nd.add_node(11)
    tree_nd.add_node(13)
    tree_nd.add_node(8)
    tree_nd.add_node(7)
    tree_nd.add_node(9)
    tree_nd.find_node(8)
    tree_nd.find_node(18)
    print("inorder traversal")
    tree_nd.inorder_print_tree()
    print("pre order traversal")
    tree_nd.preorder_print_tree()
    print("post order traversal")
    tree_nd.postorder_print_tree()
    # tree_nd.delete_node(10)
    print("final tree")
    tree_nd.inorder_print_tree()

    tree_nd.sub_tree(8).inorder_print_tree()

    print("printing sub tree")

    print(tree_nd.find_parent(8).data)
    print("printing after deleting node 8")
    tree_nd.delete_node(8).inorder_print_tree()

    print("printing after deleting node 10")
    tree_nd.delete_node(10).inorder_print_tree()

