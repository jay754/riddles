# http://cslibrary.stanford.edu/110/BinaryTrees.html
# all the code in the above link is in c or java but is pretty easy to convert to other languages

class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class binarytree:
    def __init__(self):
        self.root = None

    def addNode(self):
        return node(data)

    def insert(self, node, value):
        if node == None:
            self.addNode(value)
        else:
            if value <= node.data:
                node.left = self.insert(node.left, value)
            else:
                node.right = self.insert(node.right, value)

            return node

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

    # DFS transversels

    def preOrder(self, node):
        if node != None:
            self.preOrder(node.data)
            self.preOrder(node.left)
            self.preOrder(node.right)

    def inOrder(self, node):
        if node != None:
            self.inOrder(node.left)
            self.inorder(node.data)
            self.inOrder(node.right)

    def postOrder(self, node):
        if node != None:
            self.postOrder(node.left)
            self.postOrder(node.right)
            self.postOrder(node.data)

    def size(self, node):
        if node == None:
            return False
        else:
            self.size(node.left) + self.size(node.right) + 1
