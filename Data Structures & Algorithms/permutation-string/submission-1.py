class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        map_s1, map_s2 = Counter(s1), {}
        l, r = 0, 0

        while r < len(s2):
            if s2[r] in map_s1:
                map_s2[s2[r]] = 1 + map_s2.get(s2[r], 0)
                while map_s2[s2[r]] > map_s1[s2[r]]:
                    map_s2[s2[l]] -= 1
                    l+= 1
                # if length of window == s1 length, we found it
                if r - l + 1 == len(s1):
                    return True
                r += 1
            else:
                r += 1
                l = r
                map_s2.clear()      

        
        return False  