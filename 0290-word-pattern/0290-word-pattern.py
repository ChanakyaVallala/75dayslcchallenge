class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d={}
        temp=s.split(" ")
        if(len(pattern)!=len(temp)):
            return False
        s=set()
        s1=set()
        for i in range(len(pattern)):
            if pattern[i] in d:
                if d[pattern[i]]!=temp[i]:
                    return False
            else:
                d[pattern[i]]=temp[i]
                s.add(temp[i])
            s1.add(pattern[i])

        if(len(s1)!=len(s)):
            return False
        return True

        