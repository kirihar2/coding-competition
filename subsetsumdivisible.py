'''
Given a set of non-negative distinct integers, and a value m, determine if there is a subset of the given set with sum divisible by m.
Input Constraints
Size of set i.e., n <= 1000000, m <= 1000
Input : arr[] = {3, 1, 7, 5};
        m = 6;
Output : YES

Input : arr[] = {1, 6};
        m = 5;
Output : NO
'''

def solve(arr,m):
    n = len(arr)
    if m < n: 
        return True
    dp = [False for i in range(m)]
    for i in range(n):
        if dp[0] == True:
            return True
        temp = [False for t in range(m)]    
        for j in range(m):
            if dp[j] == True: 
                if dp[(j+arr[i])%m] == False: 
                    temp[(j+arr[i])%m] = True 
        for j in range(m):
            if temp[j] == True and dp[j] == False:
                dp[j] = True 
        dp[arr[i]%m] = True 

    return dp[0] 

arr = [3, 1, 7, 5]
m = 5
print(solve(arr,m))