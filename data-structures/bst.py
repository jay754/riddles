# https://dl.dropboxusercontent.com/u/6665854/binarytree.py

class Node:
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None

class BST:
    def __init__(self, root):
        self.root = root

    def insert(self, node, key):
        if node == None:
            node = Node(key)

        if node.key > key:
            if node.left == None:
                node.left = Node(key)
            else:
                self.insert(node.left, key)
        elif node.key < key:
            if node.right == None:
                node.right = Node(key)
            else:
                self.insert(node.right, key)

    def search(self, node, key):
        if node.key == key:
            return True

        if node.key > key:
            return self.search(node.left, key)
        elif node.key < key:
            return self.search(node.right, key)

    def get_minimum(self, node):
        current_node = node

        while current_node.left != None:
            current_node = current_node.left

        return current_node.key

    def get_maximum(self, node):
        current_node = node

        while current_node.right != None:
            current_node = current_node.right

        return current_node.key

    def preOrder(self, node):
        if node != None:
            print node.key
            self.preOrder(node.left)
            self.preOrder(node.right)

    def inOrder(self, node):
        if node != None:
            self.inOrder(node.left)
            print node.key
            self.inOrder(node.right)

    def postOrder(self, node):
        if node != None:
            self.postOrder(node.left)
            self.postOrder(node.right)
            print node.key

root = Node(5)
test = BST(root)
test.insert(root, 30)
test.insert(root, 50)
test.insert(root, 4)
test.insert(root, 43)

print test.get_maximum(root)
print test.get_minimum(root)

print test.search(root, 49)

# test.preOrder(root)
# test.inOrder(root)
# test.postOrder(root)
