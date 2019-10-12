def solve(s):
    def isPalindrome(dp,i,j):
        if i==j:
            return True
        return dp[i+1][j-1]
    dp = [[False for i in range(len(s))] for j in range(len(s))]
    curr_max = 0
    longestPalindromeIndices = [0,0]
    for i in range(len(s)-1, -1,-1):
        for j in range(i,len(s)):
            dp[i][j] = s[i] == s[j] and isPalindrome(dp,i,j)
            if dp[i][j] == True:
                if j-i+1 > curr_max:
                    longestPalindromeIndices=[i,j]
                    curr_max = j-i+1
    return s[longestPalindromeIndices[0]:longestPalindromeIndices[1]+1]
    
s = "abacacab"
print(solve(s))