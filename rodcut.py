def rodcut(n,prices):
    dp = [-1 for i in range(n+1)]
    dp[0] = 0
    for i in range(1,n+1):
        for j in range(i): 
            dp[i] = max(dp[i],prices[j]+dp[i-j-1])
    return dp[n]

arr = [1, 5, 8, 9, 10, 17, 17, 20] 
print(rodcut(len(arr),arr))