def solution(n):
    count =0
    n = int(n)
    orig = n
    b = bin(n)
    if b.count('1') == 1:
        l = n
    else:
        c = len(b)-1
        l = 1<<c 
    
    arr= {}
    s = []
    s.append([orig,0])
    while len(s)>0:
        curr = s.pop()
        if curr[0] == 1:
            if not 1 in arr:
                arr[1] = curr[1]
            else:
                arr[1] = min(arr[1],curr[1])
        else:
            a,count = curr
            if a in arr and arr[a] <= count:
                continue
            else:
                arr[a] = count
            
            if a&1 ==0:
                while a&1 == 0:
                    a = a>>1
                    count +=1
                s.append([a,count])
            else:
                if a < l:
                    s.append([a+1,count+1])
                if a > 1:
                    s.append([a-1,count+1])

    return arr[1]
# def solution(n):
#     d = {}
#     def recur(n):
#         n = int(n)
#         if n == 1:
#             return 0
#         elif n in d:
#             return d[n]
#         elif n& 1 == 0:
#             ret = 1+solution(n>>1)
#         else:
#             ret = 1+min(solution(n-1),solution(n+1))
#         d[n] = ret
#         return ret
#     return recur(n)
# from collections import deque 
# def solution(n):
#     d = deque()
#     d.appendleft([n,count])
#     while 

n = ''.join('9' for i in range(309))
print(solution(n))
# 27 28 14 7  8 4 2 1 
# 27 26 13 12 6 3 2 1
# 47 48 24 12 6 3 2 1
# 31 32 16 8  4 2 1
# 31 30 15 16 8  4 2 1


# 100 010 001
# 101 100 010 001
# 110 011 010 001
# 111 110 011 010 001

