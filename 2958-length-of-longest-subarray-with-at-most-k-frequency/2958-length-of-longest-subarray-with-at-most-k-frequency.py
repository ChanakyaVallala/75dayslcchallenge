class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        d={}
        l=0
        res=[]
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]]=1
            else:
                d[nums[i]]+=1
            if d[nums[i]]>k:
                while(nums[l]!=nums[i]):
                    d[nums[l]]-=1
                    l+=1
                d[nums[l]]-=1
                l+=1
            res.append(i-l+1)
        return max(res)



            
            