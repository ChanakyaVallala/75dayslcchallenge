class Solution:
    def processStr(self, s: str) -> str:
        def rev(a):
            return a[::-1]
            
        res=""
        for i in s:
            if i.islower():
                res+=i
            elif i=="*":
                if res:
                    res=res[0:len(res)-1]
                    #res.pop(len(res)-1)
            elif i=="#":
                res+=res
            elif i=="%":
                res=rev(res)
        return res

        