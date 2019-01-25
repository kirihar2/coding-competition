def solve(arr,i,curr_sum,target):
    if i >= len(arr)-1:
        return False
    if curr_sum == target:
        return True
    return solve(arr,i+1,curr_sum+arr[i],target) + solve(arr,i+1,curr_sum,target)
arr = [3, 34, 4, 12, 5, 2]
s = 9
print(solve)