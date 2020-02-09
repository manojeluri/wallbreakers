class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for num in range(left, right+1):
            boolean = self.checkEachNumber(num)
            if boolean:
                result.append(num)
        return result
    def checkEachNumber(self, num):
        digits = [int(d) for d in str(num)]
        for d in digits:
            if d == 0 or num%d != 0:
                return False
        return True