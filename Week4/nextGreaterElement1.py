class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = {}
        stack = []
        for num in nums2:
            while stack and num > stack[-1]:
                hashmap[stack.pop()] = num
            stack.append(num)
        res = []
        for num in nums1:
            if num in hashmap:
                res.append(hashmap[num])
            else:
                res.append(-1)
        return res