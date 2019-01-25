
##Method 1: Create all rectangles and filter out ones that are not parallel to x
##Method 2: Find all lines parallel to x, then try to find the lines that have the same start and end x values 
##Method 3: Find all y values with the same x. Like a bucket for each x value and their counts. set of 2 lines that have same y
#  with each other is a rectangle parallel to x-axis

def choose(n, k):
    """
    A fast way to calculate binomial coefficients by Andrew Dalke (contrib).
    """
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in range(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        return ntok // ktok
    else:
        return 0
def find_parallel(points):
    x_bucket={}
    for point in points:
        if point[0] not in x_bucket:
            x_bucket[point[0]] = {}
        if point[1] not in x_bucket[point[0]]: 
            x_bucket[point[0]][point[1]] = 1
        else:
            x_bucket[point[0]][point[1]]+=1
    x_bucket = [x_bucket[i] for i in x_bucket.keys()]
    ret = 0
    for i in range(len(x_bucket)):
        curr_x = x_bucket[i]
        for j in range(i+1,len(x_bucket)):
            other_x = list(v for v in x_bucket[j])
            number_lines_y = 0
            for ind in range(len(other_x)):
                y1 = other_x[ind]
                if y1 in curr_x:
                    number_lines_y += 1
            ret+= choose(number_lines_y,2)
    return ret

points = [[10,20],[10,30],[20,30],[20,40],[20,20],[10,40],[10,50],[20,50]]
print(find_parallel(points))