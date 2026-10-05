class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        a=[]
        m=0
        s=sum(cardPoints)
        c=0
        for i in cardPoints:
            c+=i
            a.append(c)

        w=len(cardPoints)-k
        l=0
        r=w-1
        u=sum(cardPoints[l:r+1])
        while(1):
            m=max(m,s-u)
            if r==len(cardPoints)-1:
                break
            u-=cardPoints[l]
            l+=1
            r+=1
            u+=cardPoints[r]
        return m