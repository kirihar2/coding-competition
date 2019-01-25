def solve(arr):
    #max of 3 numbers or
    #min of 2 numbers and max 1 or 
    #todo in one pass
    arr.sort()
    prod1 = 1
    for ind in range(3): 
        i = arr[len(arr)-ind-1]
        prod1*=i
    prod2 = 1
    for ind in range(2):
        i = arr[ind]
        prod2*=i
    prod2 *= arr[-1]
    return max(prod1,prod2)

l = [-5,-6,-7,-1,-7,-8]
print(solve(l))