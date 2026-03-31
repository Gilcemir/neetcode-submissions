class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0
        max_left = [0] * len(height)
        max_right = [0] * len(height)
    
        # l => r
        max_l = 0
        for i in range(1, len(height)):
            max_l = max(max_l, height[i - 1])
            max_left[i] = max_l
        
        max_r = 0
        for i in range(len(height) - 2, -1, -1):
            max_r = max(max_r, height[i + 1])
            max_right[i] = max_r
        
        for i in range(len(height)):
            w = min(max_left[i], max_right[i]) - height[i]
            res += w if w > 0 else 0

        return res
