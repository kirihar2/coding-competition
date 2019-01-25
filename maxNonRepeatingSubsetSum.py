def solve(arr):
    a = set()
    b = set()
    a_sum = 0
    b_sum = 0
    for i in arr: 
        if i not in a and i>=0: 
            a.add(i)
            a_sum += i
        elif i not in b:
            b.add(i)
            b_sum += i
        else: 
            a.add(i)
            a_sum += i
    return a_sum - b_sum

arr = [5, 8,-1, -1, 4]
print(solve(arr))