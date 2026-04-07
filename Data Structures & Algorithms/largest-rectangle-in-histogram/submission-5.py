class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                area = (i - stack[-1][0]) * stack[-1][1]
                res = max(area, res)
                start = stack[-1][0]
                stack.pop()
            
            stack.append((start, h))

        l = len(heights)
        for i, h in stack:
            area = (l - i) * h
            res = max(area, res)
        
        return res