def partition(arr,low,high):
    pivot = low
    left = low
    right = pivot + 1
    for i in range(low+1,high):
        if arr[i] < arr[pivot]:
            arr[i],arr[pivot] = arr[pivot],arr[i]
            
        
    return left + 1

def quick_sort(arr,low, high): 

    qi = partition(arr,low,high)    
    return qi