class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        freq_t = Counter(t)
        window = {}
        have, need = 0, len(freq_t)
        res, res_len = [-1, -1], float("inf")
        l = 0

        for r, c in enumerate(s):
            window[c] = 1 + window.get(c, 0)
            if c in freq_t and window[c] == freq_t[c]:
                have += 1

            while have == need:
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1
                window[s[l]] -= 1
                if s[l] in freq_t and window[s[l]] < freq_t[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l:r+1] if res_len != float("inf") else ""