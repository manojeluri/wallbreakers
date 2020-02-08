class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        c = 0
        digits[-1] += 1
        i = len(digits)-1
        if digits[-1] < 10:
            return digits
        while i >= 0:
            temp = digits[i]+c
            digits[i] = temp%10
            c = temp//10
            i -= 1
        if c == 1:
            digits = [1]+digits
        return digits