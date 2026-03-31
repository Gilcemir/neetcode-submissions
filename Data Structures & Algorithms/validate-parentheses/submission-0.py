class Solution:

    map = {
        ")": "(",
        "}": "{",
        "]": "["
    }

    def isValid(self, s: str) -> bool:
        q = deque()

        for item in s:
            if item not in self.map:
                q.append(item)
            else:
                if len(q) > 0 and q[-1] == self.map[item]:
                    q.pop()
                else:
                    return False


        return len(q) == 0



        