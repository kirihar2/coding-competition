'''
Count maximum points on same line
Given N point on a 2D plane as pair of (x, y) co-ordinates, we need to find maximum number of point which lie on the same line.

Examples:

Input : points[] = {-1, 1}, {0, 0}, {1, 1}, 
                    {2, 2}, {3, 3}, {3, 4} 
Output : 4
Then maximum number of point which lie on same
line are 4, those point are {0, 0}, {1, 1}, {2, 2},
{3, 3}
'''

def solve(points): 
    d = {}
    # tuple as key with (a,b) where y = ax + b
    def findline(pointa,pointb): 
        slope = float(pointb[1]-pointa[1])/(pointb[0]-pointa[0])
        yint = pointa[1]-slope*pointa[0]
        return (slope,yint)
    curr_max = 0
    k = ()
    for i in range(len(points)): 
        for j in range(i+1,len(points)):
            line = findline(points[i],points[j])
            if not line in d: 
                d[line] = 2
            else: 
                d[line] += 1
            if d[line] > curr_max: 
                k = line 
                curr_max = d[line]
    return curr_max

arr = [[1,1],[2,2],[3,3]]
print(solve(arr))
