def solve(arr,x):
    s = []
    s.append((0,len(arr)-1))
    mid = 0
    if x >= arr[-1]:
        return arr[-1]
    elif x <= arr[0]:
        return -1
    while len(s)>0: 
        left,right = s.pop()
        if left >= right -1:
            break 
        mid = int((right+left)/2)
        if x < arr[mid] and x>=arr[left]:
            s.append((left,mid))
        elif x <= arr[right] and x>=arr[mid]:
            s.append((mid,right))
    return arr[mid-1]
arr = [1, 2, 8, 10, 10, 12, 19]
x = 0
print(solve(arr,x))
        