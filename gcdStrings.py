class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        For strings S and T, we say "T divides S" if and only if S = T + ... + T  (T concatenated with itself 1 or more times)

        Return the largest string X such that X divides str1 and X divides str2.

        

        Example 1:

        Input: str1 = "ABCABC", str2 = "ABC"
        Output: "ABC"
        Example 2:

        Input: str1 = "ABABAB", str2 = "ABAB"
        Output: "AB"
        Example 3:

        Input: str1 = "LEET", str2 = "CODE"
        Output: ""

        ABABABAB   ABAB
        ABAB, AB

        AAAAAAAA     AAAA
        AAAA, AA, A

        ABCDABCD  ABCD
        ABCD 

        Find longest repeating substring and break it down into smaller substrings

        """
        
        n1, n2, i = len(str1), len(str2), 0
        ans = ''
        if n1 > n2:
            while i < n2:
                if str2[:i+1] * (n1 // len(str1[:i+1])) == str1 and str2[:i+1] * (n2 // len(str2[:i+1])) == str2:
                    ans = str2[:i+1]
                i += 1
        else:
            while i < n1:
                if str1[:i+1] * (n1 // len(str1[:i+1])) == str1 and str1[:i+1] * (n2 // len(str2[:i+1])) == str2:
                    ans = str1[:i+1]
                i += 1
        return ans

s1 = "ABABAB"
s2 = "ABAB"
sol = Solution()
print(sol.gcdOfStrings(s1,s2))