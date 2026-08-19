class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rows = {}
        for r, seat in reservedSeats:
            rows.setdefault(r, set()).add(seat)
        res = 2 * (n - len(rows))
        for seats in rows.values():
            left = all(s not in seats for s in [2, 3, 4, 5])
            right = all(s not in seats for s in [6, 7, 8, 9])
            middle = all(s not in seats for s in [4, 5, 6, 7])
            if left and right:
                res += 2
            elif left or right or middle:
                res += 1
        return res