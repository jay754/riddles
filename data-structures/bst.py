class Node:
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None

class BST:
    def __int__(self):
        self.root = None

    def insert(self, node, key):
        if node == None:
            return Node(key)

        if node.key > key:
            self.insert(node.left, key)
        elif node.key < key:
            self.insert(node.right, key)

    def search(self, node, key):
        if node.key == key:
            return True

        if node.key > key:
            self.search(node.left, key)
        elif node.key < key:
            self.search(node.right, key)

        return None

    def get_minimum(node):
        current_node = node

        while current_node.left != None:
            current_node = current_node.left

        return current_node.key

    def get_maximum(node):
        current_node = node

        while current_node.right != None:
            current_node = current_node.right

        return current_node.key
