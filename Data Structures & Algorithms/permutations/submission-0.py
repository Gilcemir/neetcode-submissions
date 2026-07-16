class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False] * len(nums)

        def solve(l: List[int]) -> None:
            if len(l) == len(nums):
                res.append(l[:])
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                
                l.append(nums[i])
                used[i] = True
                solve(l)
                l.pop()
                used[i] = False

        solve([])

        return res



        

        