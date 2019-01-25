'''
This is the variation of Rat in Maze

A Maze is given as N*N binary matrix of blocks where source block is the upper left most block i.e., maze[0][0] and destination block is lower rightmost block i.e., maze[N-1][N-1]. A rat starts from source and has to reach destination. The rat can move only in two directions: forward and down.
In the maze matrix, 0 means the block is dead end and non-zero number means the block can be used in the path from source to destination. The non-zero value of mat[i][j] indicates number of maximum jumps rat can make from cell mat[i][j].

In this variation, Rat is allowed to jump multiple steps at a time instead of 1.

Examples
Examples:

Input : { {2, 1, 0, 0},
         {3, 0, 0, 1},
         {0, 1, 0, 1},
          {0, 0, 0, 1}
        }
Output : { {1, 0, 0, 0},
           {1, 0, 0, 1},
           {0, 0, 0, 1},
           {0, 0, 0, 1}
         }

Explanation 
Rat started with M[0][0] and can jump upto 2 steps right/down. 
Let's try in horizontal direction - 
M[0][1] won't lead to solution and M[0][2] is 0 which is dead end. 
So, backtrack and try in down direction. 
Rat jump down to M[1][0] which eventually leads to solution.  

Input : { 
      {2, 1, 0, 0},
      {2, 0, 0, 1},
      {0, 1, 0, 1},
      {0, 0, 0, 1}
    }
Output : Solution doesn't exist
'''
def solve(arr,sol):
   
    def recur(arr,sol,i,j):
        if i >= n or j >= m: 
            return False
        if i == n-1 and j == m-1: 
            sol[i][j] = 1
            return True 
        sol[i][j] = 1
        moves = []
        curr = arr[i][j]
        for x in range(1,curr+1): 
            moves.append((x,0))
            moves.append((0,x))
        while len(moves) > 0:
            move = moves.pop()
            isSolved = recur(arr,sol[::],i+move[0],j+move[1])
            if isSolved: 
                return True 
        sol[i][j] = 0 
        return False
    return recur(arr,sol,0,0)
arr = [  [2, 1, 0, 0],
         [3, 0, 0, 1],
         [0, 1, 0, 1],
         [0, 0, 0, 1]
]
n = len(arr)
m = len(arr[0])
sol = [[0 for i in range(m)] for j in range(n)]
isSolved = solve(arr,sol)
if isSolved: 
    print(sol)
else: 
    print("Cannot solve")