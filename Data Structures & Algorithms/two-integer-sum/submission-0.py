class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, num in enumerate(nums):
            d = target - num
            if d in map:
                return [map[d], i]
            else:
                map.setdefault(num, i)
        
        return [0, 0]

        