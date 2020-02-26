import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        if not paragraph:
            return ""
        bannedSet = set(banned)
        frequency = {}
        wordList = re.sub("[^\w]", " ",  paragraph).split()
        for word in wordList:
            if word.lower() in frequency:
                frequency[word.lower()] += 1
            else:
                frequency[word.lower()] = 1
        max, word = float("-inf"), None
        for key in frequency.keys():
            if key not in bannedSet:
                if frequency[key] > max:
                    max = frequency[key]
                    word = key
        return word