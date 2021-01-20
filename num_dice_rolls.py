class Solution(object):
    def numRollsToTarget(self, d, f, target):
        """
        :type d: int
        :type f: int
        :type target: int
        :rtype: int
        """
        def recur(d,f,x):
            if x < d or x > d*f:
                return 0
            elif x <= f and x > 0 and d == 1:
                return 1
            return sum(recur(d-1,f,x-i) for i in range(1,f+1))
        def dynamic(dice,face,target):
            dp = [[0 for i in range(target+1)] for j in range(d+1)]
            for j in range(1,d+1):
                if j == 1:
                    dp[j] = [1 if i <=f and i>0 else 0 for i in range(target+1)]
                else:
                    for i in range(1,target+1):
                        curr = 0
                        for k in range(max(0,i-f),i):
                            curr += dp[j-1][k]
                        dp[j][i] = curr
            return dp[d][target]
        return dynamic(d,f,target) % (10**9+7)
d=1
f=6
target=3
sol = Solution()
print(sol.numRollsToTarget(d,f,target))