class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for token in tokens:
            # Remove '-' from string. isnumeric does not work for '-11', 
            # because '-' is not numeric.
            if token.lstrip('-').isnumeric():
                s.append(int(token))
            else:
                val2 = s.pop()
                val1 = s.pop()
                if token == "+":
                    s.append(val1 + val2)
                elif token == "-":
                    s.append(val1 - val2)
                elif token == "*":
                    s.append(val1 * val2)
                else:
                    s.append(int(val1/val2))
        
        return s[-1]