# http://cslibrary.stanford.edu/110/BinaryTrees.html
# all the code in the above link is in c or java but is pretty easy to convert to other languages

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class binarytree:
    def __init__(self, root):
        self.root = root

    def insert(self, node, value):
        if node == None:
            node = Node(value)

        if node.data > value:
            if node.left == None:
                node.left = Node(value)
            else:
                self.insert(node.left, value)
        elif node.data < value:
            if node.right == None:
                node.right = Node(value)
            else:
                self.insert(node.right, value)

    def search(self, node, value):
        if node == None:
            return False
        else:
            if node.data == value:
                return True
            else:
                if value < node.data:
                    return self.search(node.left, value)
                else:
                    return self.search(node.right, value)

    def childernCount(self,node):
        count = 0
        if node.left != None:
            count += 1
        elif node.right != None:
            count += 1

        return count

    def decedentsCount(self,node):
        count = 0
        if node.left != None:
            count += self.decedentsCount(node.left)
        elif node.right != None:
            count += self.decedentsCount(node.right)

        return count

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

    # DFS transversels

    def preOrder(self, node):
        if node != None:
            print node.data
            self.preOrder(node.left)
            self.preOrder(node.right)

    def inOrder(self, node):
        if node != None:
            self.inOrder(node.left)
            print node.data
            self.inOrder(node.right)

    def postOrder(self, node):
        if node != None:
            self.postOrder(node.left)
            self.postOrder(node.right)
            print node.data

    def size(self, node):
        if node == None:
            return False
        else:
            self.size(node.left) + self.size(node.right) + 1

root = Node(10)
test = binarytree(root)
test.insert(root, 30)
test.insert(root, 50)
test.insert(root, 4)
test.insert(root, 43)
test.insert(root, 38)
test.deleteNode(root, 30)
test.deleteNode(root, 10)

n = Node(38)

test.preOrder(root)
print test.decedentsCount(n)
