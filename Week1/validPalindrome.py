class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters = []
        for char in s:
            if char.isalnum():
                letters.append(char.lower())
        return letters == letters[::-1]