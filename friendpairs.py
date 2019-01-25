def solve(n):
    if dp[n] > 0: 
        return dp[n]
    if n > 2: 
        dp[n] = solve(n-1)+(n-1)*solve(n-2)
    else:
        dp[n] = n
    return dp[n]
n = 4
dp  = [-1 for i in range(n+1)]
print(solve(n))