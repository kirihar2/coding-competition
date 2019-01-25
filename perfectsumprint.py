def perfectsum(i,s,path,sol):

    if s < 0 or i < 0:
        return 0
    if s == 0 and i == 0:
        sol.append(path)
        return 1
    if s != 0 and i==0 and dp[0][s] > 0:
        path.append(arr[i])
        sol.append(path)
        return 1
    if dp[i-1][s]:
        temp = path[:]
        dp[i][s] =perfectsum(i-1,s,temp,sol)
        
    if s >= arr[i] and dp[i-1][s-arr[i]]:
        path.add(arr[i])
        dp[i][s] = perfectsum(i-1,s-arr[i],path,sol)
    return dp[i][s]
arr = [2, 3, 5, 6, 8, 10]
n = len(arr)
s = 10
dp = [[-1 for i in range(n)] for j in range(s+1)]
for i in range(n):
    dp[i][0] = 1
val = perfectsum(n-1,s,[],[])
print(val)
#failure 