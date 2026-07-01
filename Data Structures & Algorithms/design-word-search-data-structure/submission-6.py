class Node:
    def __init__(self, val:str = ""):
        self.val = val
        self.children = {}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = Node()


    def addWord(self, word: str) -> None:
        self._insert(word, 0, self.root)
        

    def search(self, word: str) -> bool:
        return self._search(word, 0, self.root)
    

    def _insert(self, word: str, i: int, node: Node) -> None:
        if i == len(word):
            return
        isWord = i == len(word) - 1

        if word[i] not in node.children:
            node.children[word[i]] = Node(word[i])
        
        if isWord:
            node.children[word[i]].isWord = True
        
        self._insert(word, i + 1, node.children[word[i]])
    

    def _search(self, word: str, i: int, node: Node) -> bool:
        if i == len(word):
            return node.isWord
        
        if not node.children:
            return False

        if word[i] == ".":
            return any([self._search(word, i + 1, child) for child in node.children.values()])
        
        if word[i] not in node.children:
            return False

        return self._search(word, i + 1, node.children[word[i]])