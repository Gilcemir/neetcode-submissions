class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(row: int, col: int, cursor: int) -> bool:
            if cursor == len(word):
                return True
            if (row >= len(board) or
                row < 0 or 
                col >= len(board[0]) or
                col < 0 or
                word[cursor] != board[row][col]):
                return False
            
            temp, board[row][col] = board[row][col], "#"
            found = (dfs(row + 1, col, cursor + 1) or
                dfs(row - 1, col, cursor + 1) or
                dfs(row, col + 1, cursor + 1) or
                dfs(row, col - 1, cursor + 1))
            board[row][col] = temp
            return found
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        
        return False