class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        Amin=6*minutes
        Ahours=(30 * hour)+(0.5 * minutes)
        res=Ahours-Amin
        return min(abs(res),360-abs(res))