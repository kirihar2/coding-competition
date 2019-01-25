# Egg drop problem 
# Given height h and n eggs determine minimum number of trial to figure out maximum height x the egg does not crack 
# 
# Problem: 
# If height = 1 and n = 1 then trial is 1
# If height = 2 and n = 1 then trial is at most 2
# As a more general case 2 things can happen when an egg is dropped from height x with n eggs 
# 1. The egg cracks 
#       - The critical floor is less than or equal to x
#       so check x-1 floors with n-1 eggs
# 2. The egg does not crack 
#   - The critical floor is greater than x
#       so check x floors to h with n eggs 
#       which equats to h-x with n eggs 
# Take maximum of 2 cases for each floor and take minimum value of all floors 

# Recursive function: 
#   eggdrop(h,n) = 
# {
#   1 + min(  max(eggdrop(h-1,n-1),eggdrop(h-x,n)) for x in range(h) )
# }
import sys
def solve(h,n):
    dp = [[sys.maxsize for i in range(n+1)] for j in range(h+1)]
    def recur(i,j):
        if i <= 1:
            return i
        if j == 0: 
            return i
        if dp[i][j]  < sys.maxsize: 
            return dp[i][j]
        ret = sys.maxsize
        for k in range(1,i+1):
            ret = min(ret,max(recur(k-1,j-1),recur(i-k,j)))
        dp[i][j] = ret
        return dp[i][j]
    return recur(h,n) + 1
h = 36
n = 2
print(solve(h,n))