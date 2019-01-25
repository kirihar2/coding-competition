def is_majority(arr,val): 
    #arr is sorted
    left = 0
    right = len(arr)-1
    mid = int((right - left)/2)
    majority_cutoff = int(len(arr)/2)
    if val < arr[mid] or val > arr[mid]:
        return False
    while left < right and val == arr[mid]: 
        right = mid
        mid = int((right-left)/2)
    while arr[mid]!= val: 
        mid+=1
    return arr[mid]==arr[mid+majority_cutoff]
arr = [1,2,2,2,3]
print(is_majority(arr,2))
        