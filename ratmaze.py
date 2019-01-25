
def isValid(m,n,i,j):
    return i>=0 and j>=0 and j<n and i< m
def isOpen(maze,i,j): # no need for this 
    return maze[i][j] == 1
def print_path(s):
    ret = []
    prev_dir = 0
    for i in range(len(s)):
        node = s[i]
        i = node[0]
        j = node[1]
        d = node[2]
        while prev_dir != (d-1)%4: 
            prev_dir = (prev_dir+ 1)%4
            ret.append("turn")
        ret.append("forward")
    print(ret)
    return ret
def solve(maze,start,end):
    
    m = len(maze)
    n = len(maze[0])
    visited = [[False for i in range(m)] for j in range(n)]
    s = []
    s.append(start)
    while len(s) > 0: 
        curr = s.pop()
        s.append(curr[:2] + [curr[2]+1])
        if curr[0] == end[0] and curr[1] == end[1]: 
            print_path(s)
            print(s)
            return True
        i = curr[0]
        j = curr[1]
        d = curr[2]
        if d == 0: 
            if isValid(m,n,i-1,j) and isOpen(maze,i-1,j) and  visited[i-1][j]==False:
                visited[i-1][j] = True
                s.append([i-1,j,0])
        elif d==1: 
            if isValid(m,n,i,j+1) and isOpen(maze,i,j+1) and visited[i][j+1]==False:
                visited[i][j+1] = True
                s.append([i,j+1,0])
        elif d==2: 
            if isValid(m,n,i+1,j) and isOpen(maze,i+1,j) and visited[i+1][j]==False:
                visited[i+1][j] = True
                s.append([i+1,j,0])
        elif d==3: 
            if isValid(m,n,i,j-1) and isOpen(maze,i,j-1) and visited[i][j-1]==False:
                visited[i][j-1] = True
                s.append([i,j-1,0])
        else: 
            visited[i][j] = False
            s.pop() 
    return False 

m = [   [ 1, 0, 1, 1, 0 ], 
        [ 1, 1, 1, 0, 1 ], 
        [ 0, 1, 0, 1, 1 ], 
        [ 1, 1, 1, 1, 1 ] ]
print(solve(m,[0,0,0],[2,3]))