class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        x=0
        for i in costs:
            coins=coins-i
            if coins>=0:
                x+=1
        return x