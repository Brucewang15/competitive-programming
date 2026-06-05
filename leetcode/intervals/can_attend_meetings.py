class Solution:
    def canAttendMeetings(self, intervals: list[list[int]]) -> bool:
        intervals.sort(key=lambda intv: intv[0])
        for i in range(len(intervals) - 1):
            intv1 = intervals[i]
            intv2 = intervals[i+1]

            if intv2[0] < intv1[1]:
                return False
        return True