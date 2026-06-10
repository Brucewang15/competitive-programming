class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:

        # better solution. 
        # sort by end time
        intervals.sort(key=lambda x: x[1])
        prev = 0
        remove = 0

        for cur in range(1, len(intervals), 1):
            if intervals[cur][0] < intervals[prev][1]:
                remove += 1
            else:
                prev = cur
        return remove


        # intervals.sort(key=lambda x: x[0])
        # prev = 0
        # remove = 0

        # for cur in range(1, len(intervals), 1):
        #     if intervals[cur][0] < intervals[prev][1]:
        #         remove += 1
        #         if intervals[cur][1] <= intervals[prev][1]:
        #             prev = cur
        #     else:
        #         prev = cur
        # return remove