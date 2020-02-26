class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        s_len = len(s)
        p_len = len(p)
        p_count = {}
        cur_count = {}
        a = ord('a')
        for i in range(26):
            p_count[chr(a + i)] = 0
            cur_count[chr(a + i)] = 0
        for ch in p:
            p_count[ch] += 1
        for i in range(s_len):
            cur_count[s[i]] += 1
            if i >= p_len:
                cur_count[s[i - p_len]] -= 1

            if p_count == cur_count:
                res.append(i + 1 - p_len)
        return res