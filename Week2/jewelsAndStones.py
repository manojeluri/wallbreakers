class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels = set(J)
        count = 0
        for stone in S:
            if stone in jewels:
                count += 1
        return count