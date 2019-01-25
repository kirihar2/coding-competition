import sys 
def mincost(cost,dest):
    def get_moves(i,j):
        ret = []
        if i > 0 and j > 0: 
            ret.append((i-1,j-1))
        elif i > 0: 
            ret.append((i-1,j))
        elif j > 0:
            ret.append((i,j-1))
        return ret
    m = len(cost)
    n = len(cost[0])
    dp = [[sys.maxsize for i in range(len(cost[0]))] for j in range(len(cost))]
    visited = [[False for i in range(m)] for j in range(n)]
    x,y = dest
    for i in range(m):
        for j in range(n):
            moves = get_moves(i,j)
            for move in moves:
                dp[i][j] = min(dp[i][j], dp[move[0]][move[1]]+cost[i][j])
    return dp[x][y]

arr = [[1,2,3],[4,8,2],[1,5,3]]
dest = [2,2]
print(mincost(arr,dest))