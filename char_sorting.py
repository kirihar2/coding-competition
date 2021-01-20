class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        char_seen = {}
        for c in S:
            if c not in char_seen:
                char_seen[c] = False
        t_string_to_sort = {}
        other = []
        for t in T:
            if t in char_seen:
                if t not in t_string_to_sort:
                    t_string_to_sort[t] = 1
                else:
                    t_string_to_sort[t] +=1
                    
            else:
                other.append(t)
        ret = ""
        for c in S:
            if c in t_string_to_sort:
                ret+="".join([c for i in range(t_string_to_sort[c])])
        ret+="".join(other)
        return ret
s="cba"
t ="abcd"
sol = Solution()
print(sol.customSortString(s,t))