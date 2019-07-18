from collections import deque
def solution(n):
    dp = [[0 for i in range(n+1)] for j in range(n+1)]
    for i in range(1,n+1):
        dp[i][i] = 1
    for i in range(3,n+1):
        for j in range(2,i):
            for k in range(j):
                dp[i][j] += dp[i-j][k]
    return sum(dp[n][i] for i in range(n))


for i in range(3,13):
    print(str(i)+" "+str(solution(i)))
