def climbingStaircase(n, k):
    def recur(n,k,curr,ret):
        if n == 0: 
            ret.append(curr)
            return
        i = 1
        while i <= k and n-i >=0:
            recur(n-i,k,curr+[i],ret)
            i+=1
        
    ret = []
    recur(n,k,[],ret)
    return ret

print(climbingStaircase(4,2))