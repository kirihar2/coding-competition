def merge(a,b):
    a_ind = 0
    b_ind = 0
    ret = []
    while a_ind < len(a) and b_ind < len(b): 
        if a[a_ind] < b[b_ind]:
            ret.append(a[a_ind])
            a_ind += 1
        else: 
            ret.append(b[b_ind])
            b_ind += 1
    while a_ind < len(a): 
        ret.append(a[a_ind])
        a_ind+=1
    while b_ind < len(b):
        ret.append(b[b_ind])
        b_ind+=1
    return ret


def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = int(len(arr)/2) 
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left,right)

arr = [5,4,3,2,1]
print(merge_sort(arr))