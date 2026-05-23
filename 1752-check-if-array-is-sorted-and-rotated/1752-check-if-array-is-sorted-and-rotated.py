class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        a=sorted(nums)
        for i in range(len(nums)-1):
            if(nums[i+1]<nums[i]):
                res=nums[i+1:]+nums[0:i+1]
                return a==res        
        return True


        

        