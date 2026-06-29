class Node:
    def __init__(self, val: str = "", isWord:bool = False):
        self.val = val
        self.children = {}
        self.isWord = isWord

class PrefixTree:

    def __init__(self):
        self.root = Node()
        

    def insert(self, word: str) -> None:
        self._insert(word, 0, self.root)


    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            else:
                curr = curr.children[c]
        return curr.isWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            
            curr = curr.children[c]
        return True

    
    def _insert(self, word: str, i: int, node: Node) -> None:
        if len(word) <= i:
            return None
        
        isWord = len(word) - 1 == i
        
        if word[i] not in node.children:
            node.children[word[i]] = Node(word[i], isWord)
        
        if isWord:
            node.children[word[i]].isWord = True
        
        self._insert(word, i + 1, node.children[word[i]])