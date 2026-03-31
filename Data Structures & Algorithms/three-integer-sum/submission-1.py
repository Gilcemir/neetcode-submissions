class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()

        i = 0
        while i < len(nums) - 2:
            """
            In a sorted array, you can early return for num[i] > 0 because
            there's no nums[i] + nums[l] + nums[r] = 0, where num[i] > 0
            given that num[i] >= num[l] >= num[l]
            """
            if nums[i] > 0: 
                break
            l, r = i + 1, len(nums) - 1
            while l < r:
                t = nums[i] + nums[l] + nums[r]
                if t < 0:
                    l += 1
                elif t > 0:
                    r -= 1
                else:
                    res.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
            i += 1
        
        return [list(x) for x in res]


