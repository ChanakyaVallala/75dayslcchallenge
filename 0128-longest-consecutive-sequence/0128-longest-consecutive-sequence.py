class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        m=-9999999
        nums.sort()
        a=set(nums)
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
                m=max(m,c)
                c=1
                i=i+1
        m=max(m,c)
        return m

