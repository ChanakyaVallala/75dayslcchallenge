class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        temp=[]
        for i in s:
            temp.append(i)
        res=["0"]*len(s)
        for i in range(len(temp)):
            res[i]=temp[(i+k)%len(s)]
        return "".join(res)
        