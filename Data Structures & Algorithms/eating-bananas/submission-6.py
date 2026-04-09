class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # max value in piles is upper limit.
        # binary seach while max_pile < h

        def isPossible(m: int) -> bool:
            s = 0
            for pile in piles:
                s+= pile // m
                s+= 0 if pile % m == 0 else 1
            return s <= h

        i, j = 1, max(piles)

        while i < j:
            mid = i + ((j - i) // 2)

            if isPossible(mid):
                j = mid
            else:
                i = mid + 1
        
        return j