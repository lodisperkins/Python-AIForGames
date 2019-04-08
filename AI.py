class Node:

    def __init__(self,newdata):
        self.data = newdata
        self.parent = None

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
      for i in nodes:
          for j in range [0,nodes.count]:
              if(nodes[j]==I):
                  continue
              else:
                  self.edges.append(Edge(i,nodes[j]))

    def adjacentedges(node):
        adedges = []
        for i in edges:
            if(i.start == node):
                adedges.append(i)
        return adedges


    
def bfs(graph,startnode):
    discovered=[]




