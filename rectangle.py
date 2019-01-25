arr1 = [[0,1,0],[0,1,0],[1,0,0],[1,1,1]]

def find_all_rectangles(arr):
    visited = [[False for j in range(len(arr[0]))] for i in range(len(arr))]
    ##Start = [x,y] = [j,i]
    def bfs(start,top_left,bottom_right):
        if start[0] < 0 or start[0] >= len(arr[0]) or start[1] < 0 or start[1] >= len(arr) or visited[start[1]][start[0]] == True or arr[start[1]][start[0]] == 0:
            return top_left,bottom_right
        x=start[0]
        y=start[1]
        visited[y][x] = True
        top_left = [min(top_left[0],start[0]),min(top_left[1],start[1])]
        bottom_right = [max(bottom_right[0],start[0]),max(bottom_right[1],start[1])]
        moves = [[x-1,y],[x+1,y],[x,y-1],[x,y+1]]
        for move in moves:
            top_left,bottom_right = bfs(move,top_left,bottom_right)
        return top_left,bottom_right
    ret = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 1 and visited[i][j] == False:
                ret.append(bfs([j,i],[j,i],[j,i]))
    return ret
print(find_all_rectangles(arr1))