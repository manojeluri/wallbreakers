class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hashmap = {}
        for char in s:
            if char in hashmap:
                hashmap[char] += 1
            else:
                hashmap[char] = 1
        for char in t:
            if char not in hashmap or hashmap[char] == 0:
                return False
            else:
                hashmap[char] -= 1
        return sum(hashmap.values()) == 0