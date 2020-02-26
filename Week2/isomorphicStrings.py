class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashmap1, hashmap2 = {}, {}
        for i in range(len(s)):
            if s[i] in hashmap1:
                hashmap1[s[i]].append(i)
            else:
                hashmap1[s[i]] = [i]
        for i in range(len(t)):
            if t[i] in hashmap2:
                hashmap2[t[i]].append(i)
            else:
                hashmap2[t[i]] = [i]
        return sorted(hashmap1.values()) == sorted(hashmap2.values())