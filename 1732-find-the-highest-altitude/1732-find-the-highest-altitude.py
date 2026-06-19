class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res=[]
        res.append(0)
        for i in range(len(gain)):
            a=res[i]+gain[i]
            res.append(a)
        return max(res)
