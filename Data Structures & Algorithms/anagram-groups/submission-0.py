import json
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = defaultdict(list)
        for str in strs:
            key = json.dumps(Counter(str), sort_keys=True)
            mapping[key].append(str)

        return [v for v in mapping.values()]
        