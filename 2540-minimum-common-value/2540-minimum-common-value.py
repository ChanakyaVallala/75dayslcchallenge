class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        s1=set(nums1)
        s2=set(nums2)
        s=s1.intersection(s2)
        if not s :
            return -1
        return min(s)
        