class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        arrows = 0
        if not points:
            return arrows
        start, end = points[0][0], points[0][1]
        i = 1
        while i < len(points):
            if points[i][0] <= end:
                start = points[i][0]
                end = min(end, points[i][1])
                i += 1
            else:
                arrows += 1
                start, end = points[i][0], points[i][1]
        return arrows + 1