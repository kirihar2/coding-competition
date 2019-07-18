'''
k-th distinct (or non-repeating) element in an array.
Given an integer array, print k-th distinct element in an array. The given array may contain duplicates and the output should print k-th element among all unique elements. If k is more than number of distinct elements, print -1.

Examples :

Input : arr[] = {1, 2, 1, 3, 4, 2}, 
        k = 2
Output : 4

First non-repeating element is 3
Second non-repeating element is 4

Input : arr[] = {1, 2, 50, 10, 20, 2}, 
        k = 3
Output : 10

Input : {2, 2, 2, 2}, 
        k = 2
Output : -1
'''

def solve(arr,k):
    d = set() 
    for i in arr:
        if i not in d: 
            d.add(i)
        if len(d) == k: 
            return i
    return -1

arr = [2,2,2,2,3,4]
k = 3
print(solve(arr,k)) 