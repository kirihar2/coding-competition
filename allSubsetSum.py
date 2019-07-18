def sumSubsets(arr, num):
    def recur(arr,start,num,curr,ret): 
        if num ==0: 
            ret.append(curr)
            return 
        while start < len(arr) and arr[start]  <= num: 
            recur(arr,start+1,num-arr[start],curr+[arr[start]],ret)
            start+=1
    ret = []
    recur(arr,0,num,[],ret)
    return ret
arr = [1,2,3,4,5]
num = 5
print(sumSubsets(arr,num))