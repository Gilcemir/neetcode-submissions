class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                area = (i - index) * height
                res = max(area, res)
                start = index
            
            stack.append((start, h))

        l = len(heights)
        for i, h in stack:
            area = (l - i) * h
            res = max(area, res)
        
        return res