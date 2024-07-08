# assignment: programming assignment 5
# author: Lynelle Goh
# date: 12/1/2022
# file: graph.py holds Vertex and Graph ADT
# input: it accepts numbers that can used for functions that have to do with a Graph ADT 
# output: can produce the sorting of numbers within a Graph ADT or just using creating a Graph

class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}
        self.color = 'white'

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices += 1
        adding_vertex = Vertex(key)

        # add it to the list
        self.vertList[key] = adding_vertex

    def getVertex(self,n):
        # check to see if it is in the list
        if n not in self.vertList:
            return None
        else:
            return self.vertList[n]

    def __contains__(self,n):
        return n in self.vertList.values()

    def addEdge(self,f,t,weight=0):
        # check to see if it's in the list
        if f not in self.vertList:
            self.addVertex(f)
        if t not in self.vertList:
            self.addVertex(t)

        # use Vertex function to fix it up
        # self.vertList[f].addNeighbor(self.vertList[t], weight)
        # self.vertList[t].addNeighbor(self.vertList[f], weight)
        self.vertList[f].addNeighbor(self.vertList[t], weight)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())
    
    def breadth_first_search(self, s):
        
        total_vertices = len(self.vertList)

        # now we want to mark all vertices that we haven't visited
        visited = [False]*(total_vertices)

        # BFS requires a queue-like structure
        list = []
        vertex = 0

        # use a list to print out result
        result = []

        # enqueue the passed in node and mark it as True
        list.append(s)
        visited[s] = True

        while len(list) > 0:
            vertex = list.pop(0)
            result.append(vertex)

            for i in self.vertList[vertex].getConnections():
                if visited[i.id] == False:
                    list.append(i.id)
                    visited[i.id] = True

        return result

    
    def depth_first_search(self):
        total_vertices = len(self.vertList)

        # now we want to mark all vertices that we haven't visited
        # visited = [False]*(total_vertices)
        for v in self.vertList.values():
            v.color = 'white'
        path = []

        for v in self.vertList.values():
            if v.color == 'white':
                self.DFS(v.id, path)
        return path
    
    def DFS(self, vid, path):
        
        # mark the item in the list as True since we visited it
        # path[vid] = 'gray'
        
        v = self.vertList[vid]
        v.color = 'gray'
        path.append(vid)

        # we want to recursively go through all vertices
        for i in v.getConnections():
            if i.color == 'white':
                self.DFS(i.id, path)

if __name__ == '__main__':

    g = Graph()
    for i in range(6):
        g.addVertex(i)
        
    g.addEdge(0,1)
    g.addEdge(0,5)
    g.addEdge(1,2)
    g.addEdge(2,3)
    g.addEdge(3,4)
    g.addEdge(3,5)
    g.addEdge(4,0)
    g.addEdge(5,4)
    g.addEdge(5,2)

    for v in g:
        print(v)

    assert (g.getVertex(0) in g) == True
    assert (g.getVertex(6) in g) == False
        
    print(g.getVertex(0))
    assert str(g.getVertex(0)) == '0 connectedTo: [1, 5]'

    print(g.getVertex(5))
    assert str(g.getVertex(5)) == '5 connectedTo: [4, 2]'

    path = g.breadth_first_search(0)
    print('BFS traversal by discovery time (preordering): ', path)
    assert path == [0, 1, 5, 2, 4, 3]
    
    path = g.depth_first_search()
    print('DFS traversal by discovery time (preordering): ', path)
    assert path == [0, 1, 2, 3, 4, 5]


