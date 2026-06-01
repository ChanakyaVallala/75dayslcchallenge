class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        a=1
        m=0
        for i in range(len(cost)):
            if(a%3!=0):
                m+=cost[i]
            a+=1
        return m
