def wordBoggle(board, words):
    words = set(words)
    n= len(board)
    m = len(board[0])
    s = set()
    def findAllAdjacent(i,j):
        adj = []
        if i > 0: 
            adj.append([i-1,j])
            if j > 0: 
                adj.append([i-1,j-1])
            if j < n-1: 
                adj.append([i-1,j+1])
        if i < n-1: 
            adj.append([i+1,j])
            if j > 0: 
                adj.append([i+1,j-1])
            if j < n-1: 
                adj.append([i+1,j+1])
        if j > 0: 
            adj.append([i,j-1])
        if j < n-1: 
            adj.append([i,j+1])
        return adj
    def recur(board,words,i,j,curr,ret):
        if curr+board[i][j] in words and curr+board[i][j] not in s: 
            ret.append(curr+board[i][j])
            s.add(curr+board[i][j])
        adj = findAllAdjacent(i,j)
        for x,y in adj: 
            if board[x][y] != None: 
                temp = [row[:] for row in board]
                temp[i][j] = None
                recur(temp,words,x,y,curr+board[i][j],ret)
    ret = []
    for i in range(n):
        for j in range(m):
            recur(board,words,i,j,"",ret)
    ret.sort()
    return ret

arr = [["G","T"], 
 ["O","A"]]
words = ["TOGGLE", 
 "GOAT", 
 "TOO", 
 "GO"]
print(wordBoggle(arr,words))