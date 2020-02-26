class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        result = []
        for n in nums2:
            if n in set1:
                result.append(n)
                set1.remove(n)
        return result