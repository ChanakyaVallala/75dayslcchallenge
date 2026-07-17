class Solution(object):
    def findPeakElement(self, nums):
        n=len(nums)
        if nums.index(max(nums))==0 or nums.index(max(nums))==n-1:
            return nums.index(max(nums))
        if n==1:
            return 0
        elif n==2:
            if nums[0]>nums[1]:
                return 0
            else:
                return 1
        else:
            for i in range(1,n-1):
                if nums[i]>nums[i+1] and nums[i]>nums[i-1]:
                    return nums.index(nums[i])
        
        