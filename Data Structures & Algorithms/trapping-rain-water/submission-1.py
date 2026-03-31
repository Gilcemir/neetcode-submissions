class Solution:
    def trap(self, hs: List[int]) -> int:
        l, r = 0, len(hs) - 1
        max_l, max_r = hs[l], hs[r]
        res = 0

        while l < r:
            if hs[l] < hs[r]:
                l += 1
                max_l = max(hs[l], max_l)
                res += max_l - hs[l]
            else:
                r -= 1
                max_r = max(max_r, hs[r])
                res += max_r - hs[r]

        return res
        