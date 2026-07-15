class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def solve(l: List[int], start: int) -> None:
            res.append(l[:])
            
            for i in range(start, len(nums)):
                l.append(nums[i])
                solve(l, i + 1)
                l.pop()

        solve([], 0)
        
        return res