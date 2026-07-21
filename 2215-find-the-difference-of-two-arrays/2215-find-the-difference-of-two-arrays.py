class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1=set(nums1)
        s2=set(nums2)
        res1=[]
        res2=[]
        for i in nums2:
            if i not in s1:
                res1.append(i)
        for i in nums1:
            if i not in s2:
                res2.append(i)
        res=[]
        res2=list(set(res2))
        res1=list(set(res1))
        res.append(res2)
        res.append(res1)
        return res
        