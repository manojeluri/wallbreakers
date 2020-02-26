class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        listChars = list(pattern)
        listWords = str.split(" ")
        stored = set()
        if len(listChars) != len(listWords):
            return False
        hashmap = {}
        for i in range(len(listChars)):
            if listWords[i] in hashmap:
                if hashmap[listWords[i]] != listChars[i]:
                    return False
            else:
                if listChars[i] in stored:
                    return False
                else:
                    hashmap[listWords[i]] = listChars[i]
                    stored.add(listChars[i])
        return True