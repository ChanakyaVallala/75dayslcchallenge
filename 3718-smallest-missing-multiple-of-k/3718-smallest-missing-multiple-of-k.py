class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        s=set(nums)
        i=1
        while(1):
            if k*i not in s:
                return k*i
            else:
                i+=1
        
            

        