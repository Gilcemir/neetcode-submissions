class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen: set[tuple[int, int]] = set()
        x, y = len(grid), len(grid[0])
    
        def dfs(r: int, c: int) -> None:
            seen.add((r, c))
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if (0 <= nr < x and 0 <= nc < y
                    and (nr, nc) not in seen
                    and grid[nr][nc] == "1"):
                    dfs(nr, nc)

        count = 0
        for i in range(x):
            for j in range(y):
                if (i, j) not in seen and grid[i][j] == '1':
                    count += 1
                    dfs(i, j)
        return count