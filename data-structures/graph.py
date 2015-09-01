class Edge:
    def __init__(self, node1, node2, w=None):
        self.node1 = node1
        self.node2 = node2
        self.w = w
        self.pair = (node1, node2)

class Node:
    def __init__(self, node):
        self.node = node
        self.edges = set()

class Graph:
    def __init__(self):
        self.graph = {}

    def getGraph(self):
        return self.graph

    def getNodes(self):
        return self.graph.keys()

    def getEdges(self):
        return self.graph.values()

    def hasNode(self, node):
        if node in self.nodes:
            return True

    def addNode(self, node):
        if node not in self.graph:
            self.graph[node] = set()

    def removeNode(self, node):
        if node in self.graph:
            del self.graph[n1]

    def addEdge(self, n1, n2):
        if n1 in self.graph:
            self.graph[n1].add(n2)
            # self.graph[n2].add(n1) # for directed graphs so that both nodes can point to each other

    def removeEdge(self, n1, n2):
        if n1 in self.graph:
            self.graph[n1].remove(n2)

    def printNodes(self):
        for i in self.getNodes():
            print i

    def printEdges(self):
        for i in self.getEdges():
            print i


g = Graph()
n1 = Node("a")
n2 = Node("c")

g.addNode(n1.node)
g.addNode(n2.node)

e1 = Edge("a", "b")
e2 = Edge("a", "c")
e3 = Edge("c", "b")

g.addEdge(e1.node1, e1.node2)
g.addEdge(e2.node1, e2.node2)
g.addEdge(e3.node1, e3.node2)

# g.printNodes()
# g.printEdges()

print g.getGraph()
