class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        freq = [0] * 3

        for num in stones:
            freq[num % 3] += 1

        if freq[0] % 2 == 0:
            return freq[1] > 0 and freq[2] > 0

        return abs(freq[1] - freq[2]) > 2