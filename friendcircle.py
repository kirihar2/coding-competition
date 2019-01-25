def findCircleNum(M):
    """
    :type M: List[List[int]]
    :rtype: int
    """
    g = {}
    visited = {}

    for i in range(len(M)):
        g[i] = set()
        visited[i] = False
    #dfs 
    #populate graph first
    for i in range(len(M)):
        for j in range(i,len(M[i])):
            if M[i][j] ==1: 
                if j not in g[i]:
                    g[i].add(j)
                if i not in g[j]:
                    g[j].add(i)
    def dfs(start):
        if visited[start] == True: 
            return 0
        visited[start]= True
        ret = 1
        for friend in g[start]:
            if visited[friend] ==False: 
                ret+=dfs(friend)
        return ret
    counter = 0
    for i in range(len(M)):
        ret = dfs(i)
        if ret > 0 :
            counter+=1
    return counter
arr = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
print(findCircleNum(arr))