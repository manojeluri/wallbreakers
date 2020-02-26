class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        A=A.split(" ")
        B=B.split(" ")
        s=A+B
        result=[]
        for i in s:
            if s.count(i)==1:
                result.append(i)
        return result