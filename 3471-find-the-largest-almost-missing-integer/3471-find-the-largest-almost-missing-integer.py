class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        l=0
        r=k
        d={}
        for i in nums:
            d[i]=0
        #return d
        while(r<=len(nums)):
            seen=set()
            for i in range(l, r):
                seen.add(nums[i])
            for i in seen:
                d[i] += 1
            l+=1
            r+=1
        res=[]
        for i in nums:
            if d[i]==1:
                res.append(i)
        if res:
            return max(res)
        return -1