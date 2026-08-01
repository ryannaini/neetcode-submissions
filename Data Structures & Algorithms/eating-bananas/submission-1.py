import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = 0
## Need to pull out the k valuue do pile calculation and check if it is less than h
        while l <= r:
            m = (l + r) // 2
            hours = 0
            print(f"midpoint value is {m}")
            for elt in piles:
                print(f"hours is {hours}")
                hours += math.ceil(elt / m)
            if hours <= h:
                res = m
                r = m - 1
            elif hours > h:
                l = m + 1
        return res


