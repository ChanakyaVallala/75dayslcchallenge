from collections import Counter
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        c=Counter(moves)
        if(c['U']==c['D'] and c['L']==c['R']):
            return True
        return False

        