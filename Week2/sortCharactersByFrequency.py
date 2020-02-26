import heapq
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        output = ""
        h = []
        hashmap = {}
        for char in s:
            if char in hashmap:
                hashmap[char] += 1
            else:
                hashmap[char] = 1
        for key in hashmap.keys():
            heapq.heappush(h, (-hashmap[key], key))
        while len(h) > 0:
            temp = heapq.heappop(h)
            output += temp[1]*(abs(temp[0]))
        return output