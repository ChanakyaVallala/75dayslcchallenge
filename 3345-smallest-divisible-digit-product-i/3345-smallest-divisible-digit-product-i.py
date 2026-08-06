class Solution:
    def smallestNumber(self, n: int, t: int) -> int:        
        c=1
        while(1):
            s=str(n)
            for i in s:
                c=c*int(i) 
            if c%t==0:
                return n
            else:
                c=1
                n+=1
        