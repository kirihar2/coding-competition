def dfs(arr,start,color,change,visited): 
    def get_moves(pos):
        row,col = pos[0],pos[1]
        ret = []
        if row >0: 
            ret.append((row-1,col))
        if col > 0: 
            ret.append((row,col-1))
        if row < n-1: 
            ret.append((row+1,col))
        if col < m-1: 
            ret.append((row,col+1))
        return ret
            
    n = len(arr)
    m = len(arr[0])
    s = []
    s.append(start)
    while len(s)>0:
        curr = s.pop()
        arr[curr[0]][curr[1]] = change
        visited[curr[0]][curr[1]] = True
        moves = get_moves(curr)
        for move in moves:
            row,col = move[0],move[1]
            if visited[row][col] == False and arr[row][col] == color: 
                s.append(move)
    return 

n,m = [4,7]
s = "7 5 3 5 6 2 9 1 2 7 0 9 3 6 0 6 2 6 1 8 7 9 2 0 2 3 7 5"
temp  = list(map(int,s.split(' ')))
arr = []
prev = 0
for i in range(1,len(temp)+1):
    if i%m == 0:
        arr.append(temp[prev:i])
        prev = i
    
x,y,k = [2,0,30]
visited = [[False for i in range(m)] for j in range(n)]
dfs(arr,[x,y],arr[x][y],k,visited)
print(arr)