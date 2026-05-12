class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i, val in enumerate(nums):
            v = abs(val)
            if nums[v - 1] < 0:
                return v
            nums[v - 1] *= -1
        
        return 0