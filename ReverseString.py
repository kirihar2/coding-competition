class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        ret = ""
        t = int(len(s)/(2*k))
        for i in range(0,t+1):
            curr = i*2*k
            if((len(s)-curr) < 2*k):
                ret+="".join(reversed(s[curr:len(s):1]))
            else:
                ret+="".join(reversed(s[curr:curr+k:1]))
                ret+=s[curr+k:curr+k+k]
        return ret

s="abcdefg"
k=2
sol = Solution()
print(sol.reverseStr(s,k))