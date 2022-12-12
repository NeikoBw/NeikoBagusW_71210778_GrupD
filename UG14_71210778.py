class Graph:
    def __init__(self) :
        self._data = {}
    def addVertex(self,key):
        if key not in self._data:
            self._data[key] = set()
    def vertex(self):
        print("\nSeluruh Node = ",end = ' ')
        for key, value in self._data.items():
            print(key,end = ' ')
        print()
    def addEdge(self, x,y):
        if x in self._data and y in self._data:
            self._data[x].add(y)
            self._data[y].add(x)
    def edge(self):
        print("Seluruh Edge =", end= ' ')
        listEdge = set()
        for key, value in self._data.items():
            for item in self._data[key]:
                if key + item not in listEdge and item+key not in listEdge:
                    listEdge.add(key+item)
        for item in listEdge :
            print(item, end= ' ')
        print()
    def bfs(self,node):
        visited = []
        queue = []
        visited.append(node)
        queue.append(node)
        print('Traversing BFS =',end=' ')
        while queue:
            q = queue.pop(0) 
            print (q, end = " ") 
            for neighbour in self._data[q]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
        print('\n')

#TEST CASE
graph = Graph()
graph.addVertex('a')
graph.addVertex('b')
graph.addVertex('c')
graph.addVertex('d')
graph.addVertex('e')
graph.addVertex('f')
graph.addVertex('g')

graph.addEdge('a', 'b')
graph.addEdge('b', 'c')
graph.addEdge('b', 'd')
graph.addEdge('c', 'g')
graph.addEdge('c', 'e')
graph.addEdge('d', 'e')
graph.addEdge('e', 'f')

graph.vertex()
graph.edge()
graph.bfs("a")