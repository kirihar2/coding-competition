def solve(arr):
    ret = [1 for i in arr]
    curr_prod =1
    for i in range(len(arr)): 
        ret[i]*=curr_prod
        curr_prod *= arr[i]
    curr_prod = 1
    for i in range(len(arr)-1,-1,-1): 
        ret[i] *= curr_prod
        curr_prod *= arr[i]
    return ret

l =   [1, 7, 3, 4]
print(solve(l))