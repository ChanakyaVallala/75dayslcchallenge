class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res=[]    
        def backtrack(start,comb,tot):
            if(tot==target):
                res.append(comb[:])
                return
            if(tot>target):
                return
            for i in range(start,len(candidates)):
                comb.append(candidates[i])
                backtrack(i,comb,tot+candidates[i])
                comb.pop()
        backtrack(0,[],0)
        return res
        