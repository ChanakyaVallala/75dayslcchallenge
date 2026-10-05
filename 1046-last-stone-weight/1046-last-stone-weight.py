class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        while(1):
            stones.sort()
            n=len(stones)
            if n==0:
                return n
            if n==1:
                return stones[0]
            a=n-1
            b=a-1
            if stones[a] != stones[b]:
                stones[b]=abs(stones[a]-stones[b])
                stones.pop()
            else:
                stones.pop()
                stones.pop()
        
        
        