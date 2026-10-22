class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        s=set()
        for i in range(1,k+1):
            s.add(i)
        c=0
        while(s):
            a=nums.pop()
            s.discard(a)
            c+=1
        return c
