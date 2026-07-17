class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []

        def solve(op: int, cl: int) -> None:
            if op == cl == n:
                res.append(''.join(path))
                return
            
            if op < n:
                path.append("(")
                solve(op + 1, cl)
                path.pop()

            if cl < op:
                path.append(")")
                solve(op, cl + 1)
                path.pop()
        
        solve(0, 0)
        return res