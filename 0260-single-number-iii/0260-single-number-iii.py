from collections import Counter
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        c=Counter(nums)
        res = [key for key,val in c.items() if val==1]
        return res



        