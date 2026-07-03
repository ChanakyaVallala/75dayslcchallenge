from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        c=dict(Counter(s))
        temp=[]
        for key,val in c.items():
            temp.append(val)
        temp.sort(reverse=True)
        flag=0
        c=0
        for i in temp:
            if i%2==1:
                c+=i-1
                if(flag==0):
                    flag=1
            else:
                c+=i

        if flag==1:
            c+=1
        return c

        