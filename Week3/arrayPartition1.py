class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        result = 0
        i = 0
        while i < len(nums):
            result += nums[i]
            i += 2
        return result