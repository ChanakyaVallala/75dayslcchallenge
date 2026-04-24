class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        """
        :type moves: str
        :rtype: int
        """
        r=0
        cl=0
        cr=0
        for i in moves:
            if i=="L":
                cl+=1
            if i=="R":
                cr+=1

        if(cl>cr):
            for i in moves:
                if i=="L" or i=="_":
                    cl+=1
                    r-=1
                if i=="R":
                    cr+=1
                    r+=1
                
        if(cl<=cr):
            for i in moves:
                if i=="L":
                    cl+=1
                    r-=1
                if i=="R" or i=="_":
                    cr+=1
                    r+=1

        return abs(r)
        