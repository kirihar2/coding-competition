'''
Given an array of n distinct elements, find length of the largest subset such that every pair in the subset is such that the larger element of the pair is divisible by smaller element.

Examples:

Input : arr[] = {10, 5, 3, 15, 20} 
Output : 3 
Explanation: The largest subset is 10, 5, 20.
10 is divisible by 5, and 20 is divisible by 10.

Input : arr[] = {18, 1, 3, 6, 13, 17} 
Output : 4
Explanation: The largest subset is 18, 1, 3, 6,
In the subsequence, 3 is divisible by 1, 
6 by 3 and 18 by 6.
'''

def solve(arr):
    arr.sort()
    n = len(arr)
    dp = [0 for i in range(n)]
    dp[n-1] = 1
    for i in range(n-2,-1,-1): 
        maximum = 0
        for j in range(i+1,n):
            if arr[j]%arr[i] == 0: 
                maximum = max(dp[j],maximum)
        dp[i] = 1+maximum
    return max(dp)


arr = [18, 1, 3, 6, 13, 17]
print(solve(arr))