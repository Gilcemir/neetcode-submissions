class Solution:
    def isPalindrome(self, s: str, i: int, j: int) -> bool:
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        
        return True
    
    
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def backtrack(path: List[str], start: int) -> None:
            if start == len(s):
                res.append(path[:])
                return
            
            for j in range(start + 1, len(s) + 1): #a substring e o range são exclusivos no upper limit
                if self.isPalindrome(s, start, j - 1):
                    path.append(s[start:j])
                    backtrack(path, j)
                    path.pop()

        backtrack([], 0)
        return res
        