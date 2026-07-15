class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def solve(l: List[int], start: int, target: int) -> None:
            if target < 0:
                return
            if target == 0:
                res.append(l[:])
                return
            
            for i in range(start, len(nums)):
                l.append(nums[i])
                solve(l, i, target - nums[i])
                l.pop()

        solve([], 0, target)
        return res        