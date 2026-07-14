class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        s = "123456789"
        res=[]
        for i in range(len(s)):
            for j in range(i+2,len(s)+1):
                h=int(s[i:j])
                if low<=h<=high:
                    res.append(h)
        return sorted(res)