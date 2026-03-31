class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        l, r = 0, 0
        freq_t = Counter(t)
        freq_s, freq_lr = {}, {}

        res = ""
        len_curr = 1001

        while r < len(s):
            if s[r] in t:
                freq_lr[s[r]] = 1 + freq_lr.get(s[r], 0)
                if s[r] not in freq_s or freq_s[s[r]] < freq_t[s[r]]:
                    freq_s[s[r]] = 1 + freq_s.get(s[r], 0)
                
                while freq_lr.get(s[l], 0) > freq_s.get(s[l], 0) or s[l] not in t:
                    if s[l] in freq_lr:                    
                        freq_lr[s[l]] = freq_lr[s[l]] - 1
                    l += 1
                
                r += 1
                if freq_s == freq_t:
                    temp = s[l:r]
                    if len(temp) < len_curr:
                        len_curr = len(temp)
                        res = temp

            else:
                r += 1
                if len(freq_s) == 0:
                    l = r
            
        return res






            