class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        temp=[]
        for i in word:
            temp.append(i)
        s=set(temp)
        temp=list(s)
        #return temp
        c=0
        for i in temp:
            if str(i).islower():
                a=ord(i)-32
                if(chr(a) in s):
                    c+=1
            elif str(i).isupper():
                a=ord(i)+32
                if(chr(a) in s):
                    c+=1
        return c//2

        