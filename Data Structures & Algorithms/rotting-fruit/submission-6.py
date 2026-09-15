class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rotten = []
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    rotten.append((r, c))

        seen = set(rotten)
        q = deque(rotten)
        rotten_count = len(q)

        t = 0
        while q:
            for _ in range(len(q)):
                v = q.popleft()
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    u = (v[0] + dr, v[1] + dc)
                    if (0 <= u[0] < m 
                    and 0 <= u[1] < n 
                    and u not in seen 
                    and grid[u[0]][u[1]] == 1):
                        rotten_count += 1
                        grid[u[0]][u[1]] = 2
                        seen.add(u)
                        q.append(u)
            t += 1
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    return -1
                    
        return t - 1 if rotten_count > 0 else 0