def travel(n):
        
    marked = [False for i in range(n)]
    moves = 0 
    city = 1
    while False in marked: 
        moves += 1
        if moves %2 == 0: 
            marked[city-1] = True
            if not False in marked:
                return city
        count = 0
        while count == 0 or marked[city-1] == True:
            count +=1 
            city+=1
            if city > n: 
                city = 1 
    return city
print(travel(3))