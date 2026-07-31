from collections import Counter
class Solution:
    def minimumPushes(self, word: str) -> int:
        f=Counter(word)
        s=sorted(f,key=lambda x: f[x], reverse=True)
        c=1
        t=1
        d={}
        for i in s:
            d[i]=t
            c+=1
            if((c-1)%8==0):
                t=t+1
        p=0
        for i in word:
            p+=d[i]
        return p
