from functools import lru_cache
class DSU(): 
    def __init__(self,n):
        self.n = n
        self.arr = [i for i in range(n)]
        self.__mark = [False for i in range(n)]
    def find(self,x):
        if self.arr[x] != x:
            return self.find(self.arr[x])
        return self.arr[x]
    def union(self,a,b):
        parent_a = self.find(a)
        parent_b = self.find(b)
        self.arr[b] = a
    def mark(self,a):
        self.__mark[a] = True
    def roots(self):
        return set([self.arr[i] for i,v in enumerate(self.__mark) if v])
class Solution(object):
    def numIslands2(self, m, n, positions):
        def in_bound(i,j):
            return i>=0 and j >=0 and i < m and j <n
        positions.sort()
        dsu = DSU(n*m)
        for r,c in positions:
            # check left
            dsu.mark(r*m+c)
            if in_bound(r,c-1):
                dsu.union(r*m+c-1,r*m+c)
            if in_bound(r-1,c):
                dsu.union((r-1)*m+c,r*m+c)
        #print(dsu.arr)
        return len(dsu.roots())


sol = Solution()
print(sol.numIslands2(3,3,[(0,0),(0,1),(1,2),(1,1)]))
