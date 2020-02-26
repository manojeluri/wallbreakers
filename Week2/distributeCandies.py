class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        kinds = set(candies)
        len_kinds = len(kinds)
        if len_kinds <= len(candies)//2:
            return len_kinds
        else:
            return len(candies)//2