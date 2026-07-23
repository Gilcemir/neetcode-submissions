class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        m = {
            '2': ["a", "b", "c"],
            '3': ["d", "e", "f"],
            '4': ["g", "h", "i"],
            '5': ["j", "k", "l"],
            '6': ["m", "n", "o"],
            '7': ["p", "q", "r", "s"],
            '8': ["t", "u", "v"],
            '9': ["w", "x", "y", "z"]
        }

        res = []

        def backtrack(path: List[str], start: int) -> None:
            if start == len(digits):
                if path:
                    res.append(''.join(path))
                return
            
            letters = m[digits[start]]
            for i in range(len(letters)):
                path.append(letters[i])
                backtrack(path, start + 1)
                path.pop()

        backtrack([], 0)
        return res