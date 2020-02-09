class Solution:
    def reverseVowels(self, s: str) -> str:
        letters = list(s)
        l, r = 0, len(s)-1
        vows = ["a","i","e","o","u","A","E","I","O","U"]
        vowels = set(vows)
        while l < r:
            if letters[l] in vowels and letters[r] in vowels:
                letters[l],letters[r] = letters[r],letters[l]
                l += 1
                r -= 1
            elif letters[l] in vowels and letters[r] not in vowels:
                r -= 1
            elif letters[l] not in vowels and letters[r] in vowels:
                l += 1
            else:
                l += 1
                r -= 1
        result = ""
        result = result.join(letters)
        return result