def houseRobber(nums):
    n = len(nums)
    dp = [-1 for i in range(n)]
    def recur(nums,id): 
        if id >= n: 
            return 0
        if dp[id] >= 0: 
            return dp[id]
        dp[id] =  max(recur(nums,id+2)+nums[id],recur(nums,id+1))
        return dp[id]
    recur(nums,0)
    return dp[0]
nums = [1,1,1]
print(houseRobber(nums))