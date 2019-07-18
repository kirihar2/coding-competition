def nQueens(n):
    grid = [[0 for i in range(n)] for j in range(n)]
    
    def recur(grid,curr,ret):
        if len(curr) == n: 
            ret.append(curr)
            return
        i = len(curr)
        for j in range(n):
            if grid[i][j] == 0: 
                temp = [row[:] for row in grid]
                temp[i] = [-1 for x in range(n)]
                
                for y in range(n):
                    temp[y][j] = -1
                x,y = i,j
                while x >=0 and y>=0: 
                    temp[x][y] = -1
                    x-=1
                    y-=1
                    
                x,y = i,j
                while x >=0 and y<n: 
                    temp[x][y] = -1
                    x-=1
                    y+=1
                    
                x,y = i,j
                while x <n and y<n: 
                    temp[x][y] = -1
                    x+=1
                    y+=1
                    
                x,y = i,j
                while x <n and y>=0: 
                    temp[x][y] = -1
                    x+=1
                    y-=1
                    
                    
                temp[i][j] = 1 
                recur(temp,curr+[j+1],ret)
                    
            
    ret = []
    recur(grid,[],ret)
    return ret
print(nQueens(4))