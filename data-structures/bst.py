# https://dl.dropboxusercontent.com/u/6665854/binarytree.py
# http://www.quora.com/How-can-you-find-successors-and-predecessors-in-a-binary-search-tree-in-order

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

    def deleteNode(self, node, value):
        if node == None:
            return node

        if value < node.data:
            node.left = self.deleteNode(node.left, value)
        elif value > node.data:
            node.right = self.deleteNode(node.right, value)
        else:
            if node.left == None:
                temp = node.right
                del node
                return temp
            elif node.right == None:
                temp = node.left
                del node
                return temp

            temp = self.get_minimum(node.right)
            node.data = temp.data
            node.right = self.deleteNode(node.right, temp.data)

        return node

    def get_minimum(self, node):
        current_node = node

        while current_node.left != None:
            current_node = current_node.left

        return current_node

    def get_maximum(self, node):
        current_node = node

        while current_node.right != None:
            current_node = current_node.right

        return current_node

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

    def succesor(self, root, node):
        succesor = None

        if node.right:
            succesor = node.right
            while node.left:
                succesor = node.left
        else:
            while root:
                if node.key < root.key:
                    succesor = root
                    root = root.left
                elif node.key > root.key:
                    root = root.right
                else:
                    break

        return succesor

    def printAllPaths(self, node):
        self.printAllPathsR(node, "")

    def printAllPathsR(self, node, pathSoFar):
        if node == None:
            print pathSoFar
        if node.left != None:
            self.printAllPathsR(node.left, pathSoFar + str(node.key) + ",")
        if node.right != None:
            self.printAllPathsR(node.right, pathSoFar + str(node.key) + ",")
        if node.left == None and node.right == None:
            print pathSoFar + str(node.key)

root = Node(5)

test = BST(root)
test.insert(root, 30)
test.insert(root, 50)
test.insert(root, 4)
test.insert(root, 43)
test.insert(root, 38)

test.printAllPaths(root)

test.remove(root, 4)

test.printAllPaths(root)

# print test.get_maximum(root)
# print test.get_minimum(root)

# print test.search(root, 49)

# test.preOrder(root)
# test.inOrder(root)
# test.postOrder(root)
