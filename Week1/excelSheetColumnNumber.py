class Solution:
    def titleToNumber(self, s: str) -> int:
        if len(s) == 0:
            return 0
        length = len(s)
        result = 0
        for i in s:
            result += (ord(i)-ord("A")+1)*(26**(length-1))
            length -= 1
        return result