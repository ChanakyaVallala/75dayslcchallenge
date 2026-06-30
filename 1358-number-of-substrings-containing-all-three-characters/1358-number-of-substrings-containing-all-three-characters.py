class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        se={"a":0,"b":0,"c":0}
        l=0
        c=0
        for r in range(len(s)):
            se[s[r]]+=1
            while se['a']>0 and se['b']>0 and se['c']>0 :
                c+=len(s)-r
                se[s[l]]-=1
                l+=1
        return c