class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        l=len(word)
        a=8
        c=1
        res=0
        while l>=a:
            l=l-a
            res=res+ 8*c
            c+=1
        if l-a<a:
            res+=(l*c)
        return res