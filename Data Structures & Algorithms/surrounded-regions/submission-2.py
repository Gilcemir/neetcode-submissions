class Solution:
    def solve(self, board: List[List[str]]) -> None:
        DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n = len(board), len(board[0])

        borders = []
        # top + down
        for i in range(n):
            if board[0][i] == 'O':
                borders.append((0, i))
            if board[m - 1][i] == 'O':
                borders.append((m - 1, i))
        
        # left + right
        for i in range(1, m - 1):
            if board[i][0] == 'O':
                borders.append((i, 0))
            if board[i][n - 1] == 'O':
                borders.append((i, n - 1))
        
        q = deque(borders)
        for r, c in q:
            board[r][c] = '#'
        
        while q:
            r, c = q.popleft()
            for dr, dc in DIRECTIONS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == 'O':
                    board[nr][nc] = '#'
                    q.append((nr, nc))
        
        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == '#':
                    board[r][c] = 'O'     