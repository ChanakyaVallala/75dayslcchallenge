from typing import List
from math import gcd
class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n=len(coins)
        def f(x):
            s=0
            for m in range(1,1<<n):
                l=1
                c=0
                for i in range(n):
                    if m>>i&1:
                        l=l//gcd(l,coins[i])*coins[i]
                        if l>x:
                            break
                        c+=1
                else:
                    if c&1:
                        s+=x//l
                    else:
                        s-=x//l
            return s
        lo,hi=1,k*min(coins)
        while lo<hi:
            m=(lo+hi)//2
            if f(m)>=k:
                hi=m
            else:
                lo=m+1
        return lo
