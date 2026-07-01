class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res=[]
        res.append(intervals[0])
        for i in range(1,len(intervals)):
            s=intervals[i][0]
            e=intervals[i][1]
            if res[-1][-1]>= s:
                res[-1][-1]=max(res[-1][-1],e)
            else:
                res.append([s,e])
        return res
