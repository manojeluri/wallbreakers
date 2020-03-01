class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        result, hashmap, max_last_seen, count = [], {}, 0, 0
        for i in range(len(S)):
            hashmap[S[i]] = i
        for i, char in enumerate(S):
            max_last_seen = max(max_last_seen, hashmap[char])
            count += 1
            if i == max_last_seen:
                result.append(count)
                count = 0
        return result