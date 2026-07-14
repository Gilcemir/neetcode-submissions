class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.board = [[0] * n for _ in range(n)]
        self.cols = set()
        self.left_diag = set() # row - col (como os dois somam 1 sempre, a diferença é sempre igual na diag)
        self.right_diag = set() # row + col (como um diminui e outro soma, a soma deles é sempre igual)
        self.cols_of = {}
        self.res = []
        self.n = n

        self.solve()

        return self.res
    
    def solve(self, row: int = 0, count: int = 0) -> int:
        if row == self.n:
            self.res.append(self.transform())
            return 1
        for col in range(self.n):
            if self.is_queen_safe(row, col):
                self.place_queen(row, col)
                count += self.solve(row + 1, count)
                self.remove_queen(row, col)
        return count

    def is_queen_safe(self, row: int, col: int) -> bool:
        return (col not in self.cols
                and (row - col) not in self.left_diag
                and (row + col) not in self.right_diag)


    def place_queen(self, row: int, col: int) -> None:
        self.board[row][col] = 1
        self.cols_of[row] = col
        self.cols.add(col)
        self.left_diag.add(row - col)
        self.right_diag.add(row + col)
        
    
    def remove_queen(self, row: int, col: int) -> None:
        self.board[row][col] = 0
        del self.cols_of[row]
        self.cols.discard(col)
        self.left_diag.discard(row - col)
        self.right_diag.discard(row + col)

        

    def transform(self) -> List[str]:
        res = []
        for row in self.board:
            res.append(''.join(['.' if x == 0 else 'Q' for x in row]))
        
        return res