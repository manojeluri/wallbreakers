class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        m = len(A)
        n = len(A[0])
        transA = [[0 for i in range(m)] for j in range(n)]
        for i in range(m):
            for j in range(n):
                transA[j][i] = A[i][j]
        return transA