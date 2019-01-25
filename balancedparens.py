def isbalanced(w):
    if len(w) == 0: 
        return True 
    if w[0] == '(' and w[-1] == ')' or (w[0] == '[' and w[-1]==']'):
        return isbalanced(w[1:-1])
    for i in range(1,len(w)):
        x = w[:i]
        y = w[i:]
        left_isbalanced = isbalanced(x)
        right_isbalanced = isbalanced(y)
        if left_isbalanced and right_isbalanced: 
            return True 
    return False
def balanced(w): 
    s = []
    for i in w:
        if i is '(' or i is '[': 
            s.append(i)
        else: 
            if len(s)==0: 
                return False 
            t = s.pop()
            if i is ')' and t is not '(':
                return False
            if i is ']' and t is not '[':
                return False 
    if len(s) > 0 :
        return False 
    return True  
                
#w ="(([[(())]][[]](())))[[(())(())]](())(()"
#print(balanced(w))