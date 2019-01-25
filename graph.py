from collections import deque
class Graph(): 
    def __init__(self): 
        self.nodes = []
        self.edges = []
    def __repr__(self): 
        ret = "Nodes: \n"
        for i in self.nodes: 
            ret += str(i) + ","
        ret += "Edges: \n"
        for i in self.edges: 
            ret += "["+",".join(i)+"]"+ ","
    def addEdge(self,edge):
        raise NotImplementedError
   
class MapGraph(Graph):
    
    def __init__(self):
        self.nodes = []
        self.edges = []
        self.graph = {}
    
    def addNode(self,node):
        self.nodes.append(node)
        self.graph[node]={}
        
    def addEdge(self,edge):
        v1,v2,w = edge
        
        if v2 in self.graph[v1]: 
            self.graph[v1][v2] = min(self.graph[v1][v2],w)
        else: 
            self.graph[v1][v2] = w
        self.graph[v2][v1] = self.graph[v1][v2]
        self.edges.append(edge)
    
    def isReachable(self,start,end):
        #BFS
        q = deque() 
        if start not in self.nodes or end not in self.nodes: 
            return False
        q.appendleft(start)
        visited = set()
        while len(q) > 0: 
            node = q.pop()
            if node in visited:
                continue
            for i in self.graph[node]: 
                if i is end: 
                    return True 
                elif i not in visited: 
                    q.appendleft(i)
            visited.add(node)
        return False
    def distance(self,start,end):
         if start not in self.nodes or end not in self.nodes: 
            return -1 
        
m= MapGraph() 
nodes = [1,2,3,4,5]
for i in nodes: 
    m.addNode(i)
edges=[[1,2,1],[2,3,1],[4,2,1]]
for i in edges: 
    m.addEdge(i)
print(m.isReachable(1,2))
print(m.isReachable(1,3))
print(m.isReachable(1,6))
print(m.isReachable(1,5))

