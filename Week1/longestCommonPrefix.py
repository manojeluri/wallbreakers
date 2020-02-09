class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        out = strs[0]
        for item in strs[1:]:
            i = 0
            while i < len(item) and i < len(out):
                if item[i] != out[i]:
                    break
                i += 1
            out = out[:i]
        return out