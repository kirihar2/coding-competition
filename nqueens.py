from copy import deepcopy

def solveNQueens( n):
    """
    :type n: int
    :rtype: List[List[str]]
    """
    grid =[[-1 for i in range(n)] for j in range(n)]
    def isValidPos(pos):
        return pos[0] >=0 and pos[0] < n and pos[1] >= 0 and pos[1] < n
    def isOpen(g,pos):
        return g[pos[0]][pos[1]] == -1
    def populate(g,pos):
        if not isValidPos(pos) or not isOpen(g,pos):
            return False
        g[pos[0]][pos[1]] = 0
        for i in range(1,n):
            if i != pos[1]:
                g[pos[0]][i] = 1
            if i != pos[0]:
                g[i][pos[1]] = 1
            if isValidPos((pos[0]+i,pos[1]+i)):
                g[pos[0]+i][pos[1]+i] = 1
            if isValidPos((pos[0]-i,pos[1]+i)):
                g[pos[0]-i][pos[1]+i] = 1
            if isValidPos((pos[0]+i,pos[1]-i)):
                g[pos[0]+i][pos[1]-i] = 1
            if isValidPos((pos[0]-i,pos[1]-i)):
                g[pos[0]-i][pos[1]-i] = 1
        return True
    def recur(g,col,sol):
        if col >= n:
            sol.append(g)
            return g,True
        for i in range(n):
            if isOpen(g,(i,col)):
                temp = deepcopy(g)
                isPossible = populate(temp,(i,col))
                if isPossible:
                    temp,populated = recur(temp,col+1,sol)
        return g,False
    sol =[]
    grid,pos = recur(grid,0,sol)
    ret=[]
    for possible_sol in sol: 
        l = []
        for i in range(len(possible_sol)):
            s = ""
            for j in range(len(possible_sol[0])):
                if possible_sol[i][j] == 0: 
                    s+='Q'
                else:
                    s+='.'
            l.append(s)
        ret.append(l)
    return ret
def solveNQueensDFS(n):
    def DFS(queens,xy_sum,xy_diff):
        p = len(queens)
        if p == n: 
            ret.append(queens)
            return None
        for q in range(n):
            if q not in queens and p+q not in xy_sum and p-q not in xy_diff: 
                DFS(queens+[q],xy_sum+[p+q],xy_diff+[p-q])
    ret = []
    DFS([],[],[])
    result = []
    for sol in ret: 
        temp = []
        for i in sol: 
            s = ""
            for j in range(n):
                if j == i: 
                    s+='Q'
                else: 
                    s+='.'
            temp.append(s)
        result.append(temp)
    return result
print(solveNQueensDFS(4))