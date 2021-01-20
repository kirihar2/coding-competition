class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        ret = 0
        available = {}
        for c in chars:
            if c in available:
                available[c] += 1
            else:
                available[c] = 1
        for word in words:
            count = {}
            flag = True
            for c in word:
                if c not in available:
                    flag = False
                    break
                elif c in count and available[c] == count[c]:
                    flag = False
                    break
                else:
                    if c in count:
                        count[c]+=1
                    else:
                        count[c] = 1
            if flag:
                ret+= len(word)
        return ret
words = ["cat","bt","hat","tree"]
chars = "atach"
sol = Solution()
sol.countCharacters(words,chars)