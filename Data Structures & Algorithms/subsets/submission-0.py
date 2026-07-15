class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        list_length = len(nums)

        def solve(l: List[int], start: int, length: int) -> None:
            if len(l) == length:
                res.append(l[:])
            
            for i in range(start, list_length):
                l.append(nums[i])
                solve(l, i + 1, length)
                l.pop()

        for k in range(list_length + 1):
            solve([], 0, k)
        
        return res