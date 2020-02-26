class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        s = n*(n+1)//2
        mis = s - sum(set(nums))
        duplicate = sum(nums) + mis - s
        return [duplicate, mis]