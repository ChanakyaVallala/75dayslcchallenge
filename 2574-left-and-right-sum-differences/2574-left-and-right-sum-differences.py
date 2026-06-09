class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        c=sum(nums)
        a=0
        res=[]
        for i in nums:
            res.append(abs(a-(c-i-a)))
            a+=i
        return res