from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        q="balloon"
        x=Counter(q)
        c=Counter(text)
        res=[]
        for ch in x:  
            res.append(c[ch] // x[ch])
        return min(res)