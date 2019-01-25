class Sudoku():
    def __init__(self,n):
        self.grid = [[0 for i in range(n)] for j in range(n)]
    def solve(self):
        def isValidLocation(x,y):
            return x >=0 and x< self.n and y >= 0 and y<self.n
        def recur(grid,x,y):
            if not isValidLocation(x,y):
                return grid 
            
        