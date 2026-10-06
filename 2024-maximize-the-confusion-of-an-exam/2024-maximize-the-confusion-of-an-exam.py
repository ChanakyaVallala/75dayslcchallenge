class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        d={}
        l=0
        res=0
        c=0
        for i in range(len(answerKey)):
            if answerKey[i] not in d:
                d[answerKey[i]]=1
            else:
                d[answerKey[i]]+=1
            c=max(c,d[answerKey[i]])
            while(i-l+1 - c>k):
                d[answerKey[l]]-=1
                l+=1
            res=max(res,i-l+1)
        return res


        