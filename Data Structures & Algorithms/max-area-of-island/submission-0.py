class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(r: int, c: int) -> int:
            if grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0
            re = 1
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc 
                if (0 <= nr < rows and 0 <= nc < cols
                    and grid[nr][nc] == 1):
                    re += dfs(nr, nc)
            return re

        res = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    res = max(res, dfs(row, col))
        return res