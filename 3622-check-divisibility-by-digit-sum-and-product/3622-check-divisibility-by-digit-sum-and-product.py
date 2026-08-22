class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        a=str(n)
        s=0
        m=1
        for i in a:
            s+=int(i)
            m=m*int(i)
        if n%(s+m)==0:
            return True
        return False

        