#http://www.geeksforgeeks.org/splay-tree-set-1-insert/
# the code has been taken from the above site. The above site
# has its code in c, but is pretty straight forward to implement in Python

# this is a data structure referred to as a splay tree.
# like a red black, it is a self-balancing Binary search Tree
# https://github.com/anoopj/pysplay/blob/master/splay.py

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

    def remove(self, node, key):
        if node == None:
            return

        if node.key > key:
            node.left = self.remove(node.left, key)
        elif node.key < key:
            node.right = self.remove(node.right, key)

    def rightRotate(self, node):
        y = node.left
        node.left = y.right
        y.right = node
        return y

    def leftRotate(self, node):
        y = node.right
        node.right = y.left
        y.left = node
        return y

    def splay(self, root, key):
        if root == None or root.key == key:
            return root

        if root.key > key:
            if root.left == None:
                return root

            if root.left.key > key:
                root.left.left = self.splay(root.left.left, key)
                root = self.rightRotate(root)
            elif root.left.key < key:
                root.left.right = self.splay(root.left.right, key)
                if root.left.right != None:
                    root.left = self.leftRotate(root.left)

            if root.left == None:
                return root
            else:
                return self.rightRotate(root)

        else:
            if root.right == None:
                return root

            if root.right.key > key:
                root.right.left = self.splay(root.right.left, key)

                if root.right.left != None:
                    root.right = self.rightRotate(root.right)

            elif root.right.key < key:
                root.right.right = self.splay(root.right.right, key)
                root = self.leftRotate(root)

            if root.right == None:
                return root
            else:
                return self.leftRotate(root)

    def search(self, root, key):
        return self.splay(root, key)

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

root = Node(100)
root.left = Node(50)
root.right = Node(200)
root.left.left = Node(40)
root.left.left.left = Node(30)
root.left.left.left.left = Node(20)

test = BST(root)
root = test.search(root, 20)

# test.preOrder(root)
# print root.right.right.key
# attrs = vars(root)

# I cannot draw trees as ascii art. Forgive me
# the tree looks like this after the splay

#         20
#           \
#           50
#         /    \
#        30    100
#         \       \
#         40      200
