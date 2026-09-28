class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            c=0
            for j in str(nums[i]):
                c+=int(j)
            if c==i:
                return i
        return -1
        