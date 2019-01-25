def coinchange(n):
    dp = [[0 for i in range(4)] for j in range(n+1) ]
    for i in range(4):
        dp[0][i] = 1
     
    change = [25,10,5,1]
    s = []
    s.append((n,3))
    while len(s)>0: 
        curr,ind = s.pop()
        if dp[n][ind] > 0: 
            for i in range(len(change)):
            
    print(dp)
n = 10
print(coinchange(n))