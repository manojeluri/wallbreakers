class Solution:
    def isValid(self, s: str) -> bool:
        hashmap, stack = {"(":")", "{":"}", "[":"]"}, []
        for c in s:
            if c in hashmap:
                stack.append(hashmap[c])
            else:
                if not stack:
                    return False
                if stack.pop() == c:
                    continue
                else:
                    return False
        return not stack