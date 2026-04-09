class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # max value in piles is upper limit.
        # binary seach while max_pile < h

        i, j = 1, max(piles)
        res = j # at least max

        while i <= j:
            mid = i + ((j - i) // 2)

            if self.isPossible(piles, h, mid):
                res = mid
                j = mid - 1
            else:
                i = mid + 1
        
        return res
    

    def isPossible(self, piles: List[int], h: int, candidate: int) -> bool:
        s = 0

        for pile in piles:
            s += pile // candidate
            s += 0 if pile % candidate == 0 else 1
        
        return s <= h