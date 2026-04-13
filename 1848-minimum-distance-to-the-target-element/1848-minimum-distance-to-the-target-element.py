class Solution(object):
    def getMinDistance(self, nums, target, start):
        """
        :type nums: List[int]
        :type target: int
        :type start: int
        :rtype: int
        """
        res=[]
        for i in range(len(nums)):
            if nums[i]==target:
                res.append(abs(i-start))
        return min(res)