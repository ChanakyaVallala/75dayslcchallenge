class Solution(object):
    def subsets(self, nums):
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
            res.append(s)
        return res