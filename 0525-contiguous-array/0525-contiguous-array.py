class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i]==0:
                nums[i]=-1
        m=0
        s={0:-1}
        c=0
        for i in range(len(nums)):
            c+=nums[i]
            if c not in s:
                s[c]=i
            else:
                m=max(m,abs(i-s[c]))
        return m


        