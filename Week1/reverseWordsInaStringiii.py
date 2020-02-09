class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        result = ""
        for word in words:
            result += word[::-1]
            result += " "
        return result[:len(result)-1]