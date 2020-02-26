from collections import defaultdict


class Solution:
    def isUpperCase(self, c: str) -> bool:
        return (c >= "A" and c <= "Z")

    def isLowerCase(self, c: str) -> bool:
        return (c >= "a" and c <= "z")

    def isInt(self, c: str) -> bool:
        return (c >= '0' and c <= '9')

    def getElement(self, str: str, i: int) -> (str, int):
        elem = str[i]
        i += 1
        while (i < len(str) and self.isLowerCase(str[i])):
            elem += str[i]
            i += 1
        return (elem, len(elem))

    def getInt(self, formula: str, i: int) -> (int, int):
        temp = i
        mult = ""
        while (temp < len(formula) and self.isInt(formula[temp])):
            mult += formula[temp]
            temp += 1
        return (int(mult or 1), len(mult))

    def formatOutput(self, stack: [defaultdict(int)]) -> str:
        output = ""
        for key, value in sorted(stack[-1].items()):
            if value == 1:
                output += key
            else:
                output += key + str(value)
        return output

    def countOfAtoms(self, formula: str) -> str:
        stack = [defaultdict(int)]
        i = 0
        length = len(formula)
        while i < length:
            if i < length and formula[i] == "(":
                stack.append(defaultdict(int))
                i += 1
            elif (i < length and formula[i] == ")"):
                temp = stack.pop()
                i += 1
                mult, increment = self.getInt(formula, i)
                i += increment
                for key, value in temp.items():
                    stack[-1][key] += value * mult
            else:
                if i < length and self.isUpperCase(formula[i]):
                    elem, increment = self.getElement(formula, i);
                    i += increment
                    mult, increment = self.getInt(formula, i)
                    print(mult)
                    i += increment
                    stack[-1][elem] += mult
                    print(stack)
        output = self.formatOutput(stack)
        return output
