class Solution(object):
    def pancakeSort(self, arr):
        res = []

        def flip(k):
            arr[:k + 1] = arr[:k + 1][::-1]

        for size in range(len(arr), 1, -1):
            max_val = size
            k = arr.index(max_val)

            # Already in the correct position
            if k == size - 1:
                continue

            # Bring max element to the front
            if k != 0:
                flip(k)
                res.append(k + 1)

            # Bring max element to its final position
            flip(size - 1)
            res.append(size)

        return res
