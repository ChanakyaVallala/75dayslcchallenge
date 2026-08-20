class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1=[]
        arr2=[]
        arr1.append(nums[0])
        arr2.append(nums[1])
        n=len(nums)
        for i in range(2,n):
            a1=len(arr1)-1
            a2=len(arr2)-1
            if arr1[a1]>arr2[a2]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])
        return arr1+arr2
                
        