class Solution(object):
    def stoneGameVIII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        n=len(stones)
        p=stones[:]
        for i in range(1, n):
            p[i]+=p[i-1]
        best = p[n-1]
        for i in range(n-2,0,-1):
            best = max(best,p[i]-best)
        return best