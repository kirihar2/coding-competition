from collections import deque
def solution(times,time_limit):
    ret = []
    if checkNegativeCycle(times):
        return [i for i in range(len(times)-2)]
    s = deque()
    bulkhead_pos = len(times)-1
    s.appendleft([0,time_limit,set(),set()])
    #Extra condition to terminate traversal
    min_traversal_time = times[0][0]
    for i in times:
        for j in i: 
            min_traversal_time = min(min_traversal_time,j)

    while len(s) > 0:
        curr_pos,t,holding_bunnies,saved_bunnies = s.pop()
        if curr_pos == bulkhead_pos and t >= 0:
            #Measure current best
            temp = []
            for x in saved_bunnies:
                if x != 0 and x!= bulkhead_pos:
                    temp.append(x-1)
            
            if len (temp)> len(ret):
                ret = temp
            elif len(temp) == len(ret):
                for i in range(len(temp)):
                    if temp[i] < ret[i]:
                        ret = temp
                        break
        for i in range(len(times)):
            if i != curr_pos and i not in saved_bunnies and i != bulkhead_pos and t - times[curr_pos][i] >= min_traversal_time:
                temp = set(holding_bunnies)
                temp.add(i)
                s.appendleft([i,t-times[curr_pos][i],temp,set(saved_bunnies)])
            elif i!= curr_pos and i not in saved_bunnies and i == bulkhead_pos and t-times[curr_pos][bulkhead_pos] >= 0:
                temp = set(saved_bunnies)
                for bunny in holding_bunnies:
                    if bunny not in temp:
                        temp.add(bunny)
                s.appendleft([bulkhead_pos,t-times[curr_pos][bulkhead_pos],set(),temp])
    return ret
def checkNegativeCycle(times):           
    # Floyd Warshall negative cycle detection
    
    V = len(times)
    dist=[[0 for i in range(V+1)]for j in range(V+1)] 
    for i in range(V): 
        for j in range(V): 
            dist[i][j] = times[i][j] 
    for k in range(V): 
        for i in range(V): 
            for j in range(V): 
                if (dist[i][k] + dist[k][j] < dist[i][j]): 
                    dist[i][j] = dist[i][k] + dist[k][j] 
    for i in range(V): 
        if (dist[i][i] < 0): 
            return True
    return False 
print(solution([[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]], 1))
print(solution([[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]], 3))
print(solution([[0, 1, 1, 1, 1, 1, 1], [1, 0, 1, 1, 1, 1, 1], [1, 1, 0, 1, 1, 1, 1], [1, 1, 1, 0, 1, 1, 1], [1, 1, 1, 1, 0, 1, 1], [1, 1, 1, 1, 1, 0, -1], [1, 1, 1, 1, 1, 1, 0] ], 6))
print(solution([[0, 1, 1, 1, 2], [1, 0, 1, 1, 3], [1, 1, 0, 1, 3], [1, 1, 1, 0, 3], [1, 1, 1, 1, 0]], 3))
##negative cycle exists to bulkhead
print(solution([[0, 1, 1, 1, 0], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [-1, 1, 1, 1, 0]], 3))
##negative cycle exists between bunnies
print(solution([[0, 1, 1, 1, 0], [1, 0, -1, 1, 1], [1, -1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]], 3))
#Revisiting start position gains time but not negative cycle 
print(solution([[0, 1, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [-1, 1, 1, 1, 0]], 3))

