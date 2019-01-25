def solve(arr):
    
    def next_possible_pos(pos):
        ret = []
        i,j = pos
        if i >0: 
            ret.append((i-1,j))
        elif i < n-1: 
            ret.append((i+1,j))
        if j > 0: 
            ret.append((i,j-1))
        elif j < m-1: 
            ret.append((i,j+1))
        return ret 
    def recur(pos):
        visited[pos[0]][pos[1]] = True
        if dp[pos[0]][pos[1]] > 0: 
            return dp[pos[0]][pos[1]]
        moves = next_possible_pos(pos)
        if len(moves) == 0: 
            return 1
        curr = 0
        for next_pos in moves: 
            if not visited[next_pos[0]][next_pos[1]]:
                curr = max(curr,recur(next_pos))
        dp[pos[0]][pos[1]] = curr + 1
        return dp[pos[0]][pos[1]] 
    n = len(arr)
    m = len(arr[0])
    dp = [[-1 for i in range(m)] for j in range(n)]
    visited = [[False for i in range(m)] for j in range(n)]

    curr = 0
    for i in range(n):
        for j in range(m): 
            if dp[i][j] == -1: 
                curr = max(curr,recur((i,j)))
    return curr

arr = [[9, 6, 5, 2]
,[8, 7, 6, 5]
,[7, 3, 1, 6]
,[1, 1, 1, 7]]
print(solve(arr))