class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = []
        if not intervals:
            return result
        point = [intervals[0][0], intervals[0][1]]
        for interval in intervals[1:]:
            if interval[0] <= point[1]:
                point[1] = max(point[1], interval[1])
            else:
                result.append(point)
                point = [interval[0], interval[1]]
        result.append(point)
        return result