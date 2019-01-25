def findTargetSumWays(nums, S):
    """
    :type nums: List[int]
    :type S: int
    :rtype: int
    """
    su = sum(nums)
    dp =[[0 for i in range(su*2)] for j in range(len(nums))]
    dp[0][nums[0]] = 1
    dp[0][-1*nums[0]] = 1
    for i in range(1,len(nums)):
        num = nums[i]
        for s in range(su):
            dp[i][s] = dp[i][s-num] + dp[i][s+num]
    return dp[len(nums)-1][S-1]
nums = [1, 1, 1, 1, 1]
S = 3
print(findTargetSumWays(nums,S))


        