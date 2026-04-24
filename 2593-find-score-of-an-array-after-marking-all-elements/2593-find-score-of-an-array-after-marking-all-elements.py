class Solution(object):
    def findScore(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=0
        temp=[0]*len(nums)
        arr=sorted((nums[i],i) for i in range(len(nums)))
        for v,i in arr:
            if temp[i]==0:
                res+=v
                temp[i] =1
                if i>0:
                    temp[i-1]=1
                if i<len(nums)-1:
                    temp[i+1]=1
        return res
        