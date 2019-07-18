'''
Number of subarrays having sum exactly equal to k
Given an unsorted array of integers, find the number of subarrays having sum exactly equal to a given number k.

Examples:

Input : arr[] = {10, 2, -2, -20, 10}, 
        k = -10
Output : 3
Subarrays: arr[0...3], arr[1...4], arr[3..4]
have sum exactly equal to -10.

Input : arr[] = {9, 4, 20, 3, 10, 5},
            k = 33
Output : 2
Subarrays : arr[0...2], arr[2...4] have sum
exactly equal to 33.

'''


def solve(arr,k):
    d = set() 
    ret = 0
    for i in arr: 
        if k-i in d: 
            ret += 1
        if i not in d: 
            d.add(i)
    return ret

arr = [10, 2, -2, -20, 10]
k = -10
print(solve(arr,k)) 