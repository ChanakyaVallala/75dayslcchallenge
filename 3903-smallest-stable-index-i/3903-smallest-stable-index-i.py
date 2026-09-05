class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        res=[]
        for i in range(len(nums)):
            a=max(nums[:i+1])-min(nums[i:])
            if a<=k:
                return i
        return -1