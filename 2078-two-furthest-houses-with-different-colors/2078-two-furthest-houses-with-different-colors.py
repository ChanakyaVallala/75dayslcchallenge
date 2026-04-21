class Solution(object):
    def maxDistance(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        m=0
        for i in range(len(colors)):
            for j in range(len(colors)):
                if(i==j):
                    pass
                if(colors[i]!=colors[j]):
                    m=max(m,abs(i-j))
        return m