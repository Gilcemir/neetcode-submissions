class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        candidates.sort()

        def solve(l: list[int], start: int, target: int) -> None:
            if target == 0:
                res.append(l[:])
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > target:
                    break
                
                l.append(candidates[i])
                solve(l, i + 1, target - candidates[i])
                l.pop()
        
        solve([], 0, target)
        return res
        