class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        for r in ops:
            if r == "C":
                stack.pop()
            elif r == "D":
                stack.append(2*stack[-1])
            elif r == "+":
                stack.append(stack[-1]+stack[-2])
            else:
                stack.append(int(r))
        return sum(stack)