class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        a=len(nums)
        u=max(nums[a-1]*nums[a-2]*nums[a-3],nums[0]*nums[1]*nums[a-1])
        return u

        