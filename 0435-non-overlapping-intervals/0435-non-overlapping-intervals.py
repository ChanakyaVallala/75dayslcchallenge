class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        end=float('-inf')
        c=0
        for s,e in intervals:
            if s<end:
                c+=1
            else:
                end=e
        return c
        
        