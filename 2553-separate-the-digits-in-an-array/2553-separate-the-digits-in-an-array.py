class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        temp=[]
        for i in nums:
            if(i<10):
                temp.append(i)
            else:
                for j in str(i):
                    temp.append(int(j))
        return temp

        