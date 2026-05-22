class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        n=1<<len(nums)
        for i in range(n):
            s=[]
            for j in range(i):
                if(i&(1<<j)):
                    s.append(nums[j])
            s.sort()
            if s not in res:
                res.append(s)
        return res
        
        