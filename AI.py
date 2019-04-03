class Node:

    def __init__(self,newdata):
        self.data = newdata

class Edge:

    def __init__(self,node1,node2):
        self.start = node1
        self.end = node2

class Graph:

    def __init__(self,nodes=[]):
        self.nodes = nodes
        self.edges = []
        self.initializegraph()

    def initializegraph(self):
        i = 0
        while i <self.nodes.count:
            j=0
            while j < self.nodes.count:
                if(j == i):
                    j+=1
                else:
                    self.edges.append(Edge(nodes[i],nodes[j]))
                    j+=1
            i+=1



node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

nodes = []
nodes.append(node1)
nodes.append(node2)
nodes.append(node3)

mygraph = Graph(nodes)

iterator = mygraph.nodes[0]
print (iterator.data)
iterator = mygraph.edges[0].end
print (iterator.data)
iterator = iterator.edges[2].end
print (iterator.data)
