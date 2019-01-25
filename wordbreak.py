'''
Given a valid sentence without any spaces between the words and a dictionary of valid English words, find all possible ways to break the sentence in individual dictionary words.

Example

Consider the following dictionary 
{ i, like, sam, sung, samsung, mobile, ice, 
  cream, icecream, man, go, mango}

Input: "ilikesamsungmobile"
Output: i like sam sung mobile
        i like samsung mobile

Input: "ilikeicecreamandmango"
Output: i like ice cream and man go
        i like ice cream and mango
        i like icecream and man go
        i like icecream and mango
'''

def solve(s,d):
    sol = []
    n = len(s)
    def recur(s,d,start,curr,sol):
        if start >= n: 
            sol.append(' '.join(curr))
            return 
        for end in range(start,n):
            word = s[start:end+1]
            if word in d: 
                recur(s,d,end+1,curr+[word],sol)
        return 
    recur(s,d,0,[],sol)
    return sol

temp  = "i, like, sam, sung, samsung, mobile, ice, cream, icecream, man, go, mango, and".split(",")
d = set() 
for i in temp: 
    d.add(i.strip())
s = "ilikeicecreamandmango"
print(solve(s,d))