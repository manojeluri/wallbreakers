class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        stackS, stackT = [],[]
        for char in S:
            if char == "#":
                if stackS:
                    stackS.pop()
            else:
                stackS.append(char)
        for char in T:
            if char  == "#":
                if stackT:
                    stackT.pop()
            else:
                stackT.append(char)
        return stackS == stackT