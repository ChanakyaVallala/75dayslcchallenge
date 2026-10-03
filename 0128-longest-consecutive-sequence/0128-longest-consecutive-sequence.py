class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        a=set(nums)
        res=[]
        i=0
        b=nums[i]
        c=1
        while(i<len(nums)-1):
            if b+1 in a:
                c+=1
                i+=1
                b+=1
            else:
                b=nums[i+1]
                res.append(c)
                c=1
                i=i+1
        res.append(c)
        return max(res)

