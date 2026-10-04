class Solution:
    def reverseBits(self, n: int) -> int:
        a=bin(n)[2:]
        k=32-len(a)
        for i in range(k):
            a="0"+a
        res=""
        for i in range(31,-1,-1):
            res+=a[i]
        return int(res,2)
        