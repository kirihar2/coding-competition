'''
Golomb sequence
In mathematics, the Golomb sequence is a non-decreasing integer sequence where n-th term is equal to number of times n appears in the sequence.

The first few values are
1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, ……

Explanation of few terms:
Third term is 2, note that three appears 2 times.
Second term is 2, note that two appears 2 times.
Fourth term is 3, note that four appears 3 times.

Given a positive integer n. The task is to find the first n terms of Golomb sequence.

Examples :

Input : n = 4
Output : 1 2 2 3

Input : n = 6
Output : 1 2 2 3 3 4


a(1) = 1
a(n+1) = 1 + a(n+1-a(a(n)))
'''

def solve(n): 
    dp = [0 for i in range(n+1)]
    dp[1] = 1
    for i in range(2,n+1): 
        dp[i] = 1+ dp[i-dp[dp[i-1]]]
    return dp[1:]
print(solve(4))
print(solve(6))