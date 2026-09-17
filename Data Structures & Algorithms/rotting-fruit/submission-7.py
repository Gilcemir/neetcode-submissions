class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        fresh = sum(v == 1 for row in grid for v in row)
        q = deque([(r, c) for r in range(m) for c in range(n)if grid[r][c] == 2])

        t = 0
        while q and fresh:
            for _ in range(len(q)):
                r, c = q.popleft()
                directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        fresh -= 1
                        grid[nr][nc] = 2
                        q.append((nr, nc))
            t += 1
        
        return -1 if fresh else t