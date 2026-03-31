from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return self._get_dict(s) == self._get_dict(t)

    def _get_dict(self, s: str) -> dict:
        map = defaultdict(int)
        for item in s:
            map[item] += 1
        return map