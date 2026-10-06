class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d={}
        l=0
        c=-1
        res=0
        for r in range(len(s)):
            if s[r] not in d:
                d[s[r]]=1
            else:
                d[s[r]]+=1
            c=max(c,d[s[r]])
            while r-l+1 - c >k:
                d[s[l]]-=1
                l+=1
            res=max(res,r-l+1)
        return res

        