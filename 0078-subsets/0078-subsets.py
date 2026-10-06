class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        n=len(nums)
        res=[]
        for mask in range(1<<n):
            s=[]
            for i in range(n):
                if mask & 1<<i:
                    s.append(nums[i])
            res.append(s)
        return res