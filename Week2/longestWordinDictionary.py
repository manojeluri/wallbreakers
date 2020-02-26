class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        Set= set()
        result = ""
        Set.add("")
        for word in words:
            if word[:-1] in Set:
                if len(word) > len(result):
                    result = word
                Set.add(word)

        return result