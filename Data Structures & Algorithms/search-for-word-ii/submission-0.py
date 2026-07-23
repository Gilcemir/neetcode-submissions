class Node:
    def __init__(self, v: str = ""):
        self.v = v
        self.children = {}
        self.isWord = False
        
class Solution:

    def __init__(self):
        self.wordDict = Node()

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = set()

        for word in words:
            self.insert(word)

        def dfs(path: List[str], row: int, col: int, curr: Node) -> None:
            if curr.isWord:
                res.add(''.join(path))

            if (row < 0 or 
            row >= len(board) or 
            col < 0 or 
            col >= len(board[0]) or
            board[row][col] not in curr.children):
                return
            
            prev, curr = curr, curr.children[board[row][col]]
            tmp, board[row][col] = board[row][col], "#"
            path.append(tmp)

            dfs(path, row + 1, col, curr)
            dfs(path, row - 1, col, curr)
            dfs(path, row, col + 1, curr)
            dfs(path, row, col - 1, curr)

            board[row][col] = tmp
            curr = prev
            path.pop()
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs([], i, j, self.wordDict)

        return [x for x in res]

    def insert(self, s: str) -> None:
        self._insert(s, 0, self.wordDict)
    
    def _insert(self, s: str, i: int, curr: Node) -> None:
        if i == len(s):
            return
        
        isWord = i == len(s) - 1

        if s[i] not in curr.children:
            curr.children[s[i]] = Node(s[i])
        
        if isWord:
            curr.children[s[i]].isWord = True
        
        self._insert(s, i + 1, curr.children[s[i]])