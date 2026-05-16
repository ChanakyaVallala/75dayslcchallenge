class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res=[]
        def backtrack(start,comb,tot):
            if(tot==target):
                res.append(comb[:])
                return
            if(tot>target):
                return
            for i in range(start,len(candidates)):
                if(i>start and candidates[i]==candidates[i-1]):
                    continue
                comb.append(candidates[i])
                backtrack(i+1,comb,tot+candidates[i])
                comb.pop()
        backtrack(0,[],0)
        return res
