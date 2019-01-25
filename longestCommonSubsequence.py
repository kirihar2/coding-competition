# notes for longest common susbsequence 

# Recursion: 
# Given 2 strings stringa and stringb 
# index variable i and j for respective strings 
# If stringa[i] == stringb[j] then add to subsequence 
# Else -> max length with   i+1,j  or i,j+1
#           
# Need 2 dimensions of storage 

# Recursive function 
# LCS(n,m) = 
# { 
#   0 if n == 0 or m ==0
#   LCS(n-1,m-1)+1 if stringa[n] == stringb[m]
#   max(LCS(n-1,m),LCS(n,m-1))
# }

def solve(a,b):
    dp = [[-1 for i in range(len(b))] for j in range(len(a))]
    def recur(i,j):
        if i < 0 or j <0: 
            return 0
        if dp[i][j] >= 0: 
            return dp[i][j]
        if a[i] == b[j]: 
            return recur(i-1,j-1) + 1
        dp[i][j] = max(recur(i-1,j),recur(i,j-1))
        return dp[i][j]
    return recur(len(a)-1,len(b)-1)

a = "AGGTAB"
b = "GXTXAYB"
print(solve(a,b))