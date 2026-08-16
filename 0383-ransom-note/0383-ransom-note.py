class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c=Counter(magazine)
        for i in ransomNote:
            if i in c:
                if c[i]==0:
                    return False
                c[i]-=1  
            else:
                return False  
        return True