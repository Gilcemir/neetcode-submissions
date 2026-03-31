class Solution:
    sep = '|'
    def encode(self, strs: List[str]) -> str:
        builder = []
        for s in strs:
            builder.append(str(len(s)))
            builder.append(self.sep)
            builder.append(s)
        return ''.join(builder)

    def decode(self, s: str) -> List[str]:
        res = list()
        i = 0
        while i < len(s):
            nums = []
            while s[i].isdigit():
                nums.append(s[i])
                i += 1
                continue
            if s[i] == self.sep:
                length = int(''.join(nums))
                i += 1
                res.append(s[i: i + length])
                i += length
        
        return res
            
