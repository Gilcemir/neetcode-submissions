class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m, n = len(heights), len(heights[0])
        pacific = set([(0, c) for c in range(n)] + [(r, 0) for r in range(m)])
        pacific_q = deque(pacific)

        while pacific_q:
            r, c = pacific_q.popleft()
            for nr, nc in DIRECTIONS:
                dr, dc = r + nr, c + nc
                if (0 <= dr < m and 0 <= dc < n
                and (dr, dc) not in pacific
                and heights[dr][dc] >= heights[r][c]):
                    pacific.add((dr, dc))
                    pacific_q.append((dr, dc))
            
        
        atlantic = set([(m - 1, c) for c in range(n)] + [(r, n - 1) for r in range(m)])
        atlantic_q = deque(atlantic)

        while atlantic_q:
            r, c = atlantic_q.popleft()
            for nr, nc in DIRECTIONS:
                dr, dc = r + nr, c + nc
                if (0 <= dr < m and 0 <= dc < n
                and (dr, dc) not in atlantic
                and heights[dr][dc] >= heights[r][c]):
                    atlantic.add((dr, dc))
                    atlantic_q.append((dr, dc))


        return list(atlantic & pacific)