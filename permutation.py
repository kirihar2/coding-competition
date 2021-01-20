class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
                
        """
        if not nums:
            return []
        ret = []
        n = len(nums)
        ## ind = 001 011 111
        # curr = [] [1]
        def recur(ind,curr):
            if not ind:
                ret.append(curr)
                return
            else:
                for i in range(n):
                    x = 1<<i
                    if x&ind:
                        recur(ind|x,curr+[nums[i]])
        full = 0
        for i in range(n):
            full = full <<1
            full += 1
        recur(full,[])
        return ret