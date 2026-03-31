class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9): #rows
            rows = [False] * 10
            for j in range(9):
                if not board[i][j].isdigit():
                    continue
                v = int(board[i][j])
                if rows[v]:
                    return False
                else:
                    rows[v] = True
        
        for i in range(9): #columns
            columns = [False] * 10
            for j in range(9):
                if not board[j][i].isdigit():
                    continue
                v = int(board[j][i])
                if columns[v]:
                    return False
                else:
                    columns[v] = True
        
        for a in range(3):
            for b in range(3):
                sb = [False] * 10
                for i in range(3):
                    for j in range(3):
                        item = board[(3 * a) + i][(3 * b) + j]
                        if not item.isdigit():
                            continue
                        v = int(item)
                        if sb[v]:
                            return False
                        else:
                            sb[v] = True
        
        return True

        