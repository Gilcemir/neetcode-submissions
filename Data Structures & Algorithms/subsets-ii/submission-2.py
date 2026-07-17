class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums.sort()

        def solve(l: List[int], start: int) -> None:
            res.append(l[:])

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                
                l.append(nums[i])
                solve(l, i + 1)
                l.pop()
        
        solve([], 0)

        return res