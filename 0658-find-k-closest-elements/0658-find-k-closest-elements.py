class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """

        # Find the first element >= x
        a = 0
        while a < len(arr) and arr[a] < x:
            a += 1

        left = a - 1
        right = a

        res = []

        while k > 0:
            if left < 0:
                res.append(arr[right])
                right += 1
            elif right >= len(arr):
                res.append(arr[left])
                left -= 1
            else:
                if abs(arr[left] - x) <= abs(arr[right] - x):
                    res.append(arr[left])
                    left -= 1
                else:
                    res.append(arr[right])
                    right += 1
            k -= 1

        return sorted(res)