class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        letters = list(word)
        upper = True
        #condition 1
        for char in letters:
            if char.islower():
                upper = False
                break
        if upper:
            return upper
        #condition 2
        lower = True
        for char in letters:
            if char.isupper():
                lower = False
                break
        if lower:
            return lower
        #condition 3
        flag = True
        for char in letters[1:]:
            if char.isupper():
                flag = False
                break
        if not flag:
            return flag
        return True