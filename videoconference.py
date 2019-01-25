names = ["mary"
,"alvin"
,"alice"
,"alvin"
,"stacy"
,"sam"
,"samuel"
,"sam"]

def solve(names):
    d = {}
    ret = []
    def pop(name):
        for i in range(len(name)):
            if name[:i] not in d:
                d[name[:i]]=0
        d[name]=1
        
    for name in names: 
        if name not in d or name in d and d[name] == 0: 
            for i in range(1,len(name)):
                if name[:i] not in d or name[:i] in d and d[name[:i]] == 0:
                    pop(name)
                    ret.append(name[:i])
                    break
        else: 
            ind = 2
            curr = name+" "+str(ind)
            while curr in d:
                ind+=1
            d[curr] = 1
            ret.append(curr)
    return ret 
print(solve(names))
        
                
                    