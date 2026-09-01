class Solution:

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        treasures: list[tuple[int, int]] = []

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    treasures.append((r, c))

        seen: set[tuple[int, int]] = set(treasures)
        queue: deque[tuple[int, int]] =  deque(treasures)

        d = 0
        while queue:
            for _ in range(len(queue)):
                v = queue.popleft()
                grid[v[0]][v[1]] = d
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    u = (v[0] + dr, v[1] + dc)
                    if (0 <= u[0] < m and 0 <= u[1] < n
                    and grid[u[0]][u[1]] != -1 and u not in seen):
                        seen.add(u)
                        queue.append(u)
            d += 1
