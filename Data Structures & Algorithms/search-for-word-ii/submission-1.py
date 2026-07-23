class Node:
    def __init__(self):
        self.children = {}
        self.word = None
        
class Solution:

    def __init__(self):
        self.wordDict = Node()

    def insert(self, word: str) -> None:
        node = self.wordDict
        for ch in word:
            node = node.children.setdefault(ch, Node())
        node.word = word

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []

        for word in words:
            self.insert(word)

        def dfs(row: int, col: int, node: Node) -> None:
            ch = board[row][col]
            nxt = node.children.get(ch) # None se não existe
            if nxt is None:
                return
            if nxt.word:
                res.append(nxt.word)
                nxt.word = None # retira da Trie para não haver repetição

            board[row][col] = "#"

            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = row + dr, col + dc
                if 0 <= nr < len(board) and 0 <= nc < len(board[0]) and board[nr][nc] != "#":
                    dfs(nr, nc, nxt)
                
            board[row][col] = ch

        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, self.wordDict)

        return res