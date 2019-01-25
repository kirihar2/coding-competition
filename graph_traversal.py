from collections import deque
class Node():
    def __init__(self,x):
        self.val = x
        self.neighbors = []
    
class Graph():

    def __init__(self,matrix):
        self.matrix_2d = []
        for row in range(len(matrix)):
            self.matrix_2d.append([])
            for col in range(len(matrix[row])):
                self.matrix_2d[row].append(matrix[row][col])
    def get_neighbors(self,pos):
        row=pos[0]
        col = pos[1]
        neighbors = []
        if row >0: 
            neighbors.append((row-1,col))
        if row < len(self.matrix_2d) -1: 
            neighbors.append((row+1,col))
        if col < len(self.matrix_2d[0]) -1: 
            neighbors.append((row,col+1))
        if col > 0: 
            neighbors.append((row,col-1))
        return neighbors
    def DFS_matrix(self): # snake pattern
        
        stack = []
        visited = [[False for i in range(len(self.matrix_2d[0]))] for j in range(len(self.matrix_2d))]
        stack.append((0,0))
        path = []
        while len(stack)>0: 
            curr = stack.pop()
            visited[curr[0]][curr[1]] = True

            path.append(curr)
            neighbors = self.get_neighbors(curr)
            for neighbor in neighbors: 
                row = neighbor[0]
                col = neighbor[1]
                if not visited[row][col]: 
                    stack.append(neighbor)
                    visited[row][col] = True 
        return path 
    def BFS_matrix(self): 
        queue = deque()
        visited = [[False for i in range(len(self.matrix_2d[0]))] for j in range(len(self.matrix_2d))]
        queue.append((0,0))
        path = []
        while len(queue)>0: 
            curr = queue.popleft()
            path.append(curr)
            neighbors = self.get_neighbors(curr)
            visited[curr[0]][curr[1]] = True
            for neighbor in neighbors: 
                row = neighbor[0]
                col = neighbor[1]
                if not visited[row][col]: 
                    queue.append(neighbor)
                    visited[row][col] = True
        return path 
mat = [[1,2,3],[4,5,6],[7,8,9]]
g = Graph(mat)
print(g.DFS_matrix())
print(g.BFS_matrix())


