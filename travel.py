def find_minimal_increment(arr):
    unique = set()
    dup = []
    for i in arr:
        if i not in unique:
            unique.add(i)
        else:
            dup.append(i)
    dup.sort()
    for i in dup: 
        
        