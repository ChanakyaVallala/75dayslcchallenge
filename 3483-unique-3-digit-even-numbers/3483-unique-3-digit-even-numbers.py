from itertools import permutations
class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        res=set()
        for i in permutations(digits,3):
            n=i[0]*100 + i[1]*10 + i[2]*1
            if i[0]!=0 and i[2]%2==0:
                res.add(n)
        return len(res)
        
        


        