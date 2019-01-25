from collections import deque
class RLEIterator:

    def __init__(self, A):
        """
        :type A: List[int]
        """
        self.d = []
        for i in range(1,len(A),2):
            for j in range(A[i-1]):
                self.d.append(A[i])
        

    def next(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if len(self.d) >= n:
            ret = self.d[n-1]
            self.d = self.d[n:]
        else:
            ret = -1
            self.d = []
        return ret

A = [3,8,0,9,2,5]
c = [[2],[1],[1],[2]]
r = RLEIterator(A)
for i in c:
    print(r.next(i[0]))
