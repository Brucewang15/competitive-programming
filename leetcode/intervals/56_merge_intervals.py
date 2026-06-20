class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        merged = []
        intervals.sort(key=lambda x: x[0])

        temp = intervals[0]
        for i in range(1, len(intervals), 1):
            if intervals[i][0] > temp[1]:
                merged.append(temp)
                temp = intervals[i]
            else:
                temp[1] = max(temp[1], intervals[i][1])
        merged.append(temp)
        return merged
