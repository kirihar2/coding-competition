def solve(arr):
    dp = [[0 for i in range(len(arr[0]))] for j in range(len(arr))]
    for i in range(len(arr)):
        dp[i][0] = arr[i][0]
    ret = 0
    for i in range(1,len(arr)):
        for j in range(len(arr)):
            if j> 0 and j<len(arr)-1: 
                dp[j][i] = max(dp[j-1][i-1]+arr[j][i],dp[j+1][i-1]+arr[j][i],dp[j][i-1]+arr[j][i])
            elif j>0: 
                dp[j][i] = max(dp[j-1][i-1] + arr[j][i],dp[j][i-1]+arr[j][i])
            else:
                dp[j][i] = max(dp[j+1][i-1] + arr[j][i],dp[j][i-1]+arr[j][i])
            if i == len(arr)-1: 
                ret = max(ret,dp[j][i])
    return ret

arr = [[1,3,3],[2,1,4],[0,6,4]]
arr = [[10,33,13,15],[22,21,4,1],[5,0,2,3],[0,6,14,2]]
print(solve(arr))