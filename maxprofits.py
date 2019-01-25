profits = [
    [10644862, 56520800, 55178337, 46934767],
    [27810341, 939077  , 48546321, 51791499],
    [38618924, 41477251, 19945218, 89390306],
    [9972799 , 98576194, 93788097, 31641826],
    [92502461, 83375778, 59042823, 67955426]
]
w = len(profits)
dp = [[-1 for i in range(4)] for j in range(w)]
def recur(i,j):
    if i == 0:
        dp[i][j] = profits[i][j]
        return dp[i][j]
    if dp[i][j] > -1: 
        return dp[i][j]
    max_val = 0
    for x in range(4):
        if x == j:
            continue 
        max_val = max(max_val,recur(i-1,x))
    dp[i][j] = max_val + profits[i][j]
    return max_val
for i in range(4):    
    recur(w-1,i)
print(max(dp[-1]))