class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        m = len(A)
        n = len(A[0])
        #flipping the rows
        for i in range(m):
            for j in range(n//2):
                A[i][j], A[i][n-j-1] = A[i][n-j-1], A[i][j]
        #inverting the image
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1:
                    A[i][j] = 0
                else:
                    A[i][j] = 1
        return A