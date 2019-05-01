import math
def get_neighbors(nodes,node):
    dim = int(math.sqrt(len(nodes)))
    neighbors = []
    for i in range(0,len(nodes)):
        if i == nodes.index(node) -1:
            if((i+1) % dim == 0):
                continue
            else:
                neighbors.append(nodes[i])
        elif i == nodes.index(node)+1:
            if(i%dim == 0):
                continue
            else:
                neighbors.append(nodes[i])
        elif i == nodes.index(node) + dim:
            neighbors.append(nodes[i])
        elif i== nodes.index(node)-dim:
            neighbors.append(nodes[i])
    return neighbors
mylist = [1,2,3,4,5,6,7,8,9]
print(get_neighbors(mylist,4))

