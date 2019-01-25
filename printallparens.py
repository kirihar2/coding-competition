def parens(n):
    ret = []
    s = []
    s.append(['',n,n])
    while len(s) > 0: 
        curr,leftrem,rightrem = s.pop()
        if rightrem <leftrem:
            continue
        if len(curr) == 2*n:
            ret.append(curr)
            continue
        else: 
            if leftrem > 0: 
                s.append([curr+'(',leftrem-1,rightrem])
            if rightrem > 0: 
                s.append([curr+')',leftrem,rightrem-1])
    return ret
n = 3
print(parens(n))