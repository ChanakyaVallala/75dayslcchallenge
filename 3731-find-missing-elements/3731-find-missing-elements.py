class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        s=set()
        a=0
        b=nums[0]
        for i in nums:
            if i>a:
                a=i
            s.add(i)
            if i<b:
                b=i
        res=[]
        for i in range(b,a+1):
            if i not in s:
                res.append(i)
        return res
        
        