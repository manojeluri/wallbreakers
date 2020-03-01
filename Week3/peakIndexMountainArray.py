class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        l, r = 0, len(A)-1
        while True:
            m = (l+r)//2
            if A[m-1]<A[m]>A[m+1]:
                return m
            if A[m-1] < A[m] < A[m+1]:
                l = m+1
            if A[m-1] > A[m] > A[m+1]:
                r = m-1