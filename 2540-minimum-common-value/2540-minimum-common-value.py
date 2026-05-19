class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        m=len(nums1)
        n=len(nums2)
        a=0
        b=0
        while(a<m and b<n):
            if(nums1[a]<nums2[b]):
                a+=1
            elif nums1[a]>nums2[b]:
                b+=1
            elif nums1[a]==nums2[b]:
                return nums1[a]
        return -1