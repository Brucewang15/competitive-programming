class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        merged = []

        i = 0
        n = len(intervals)

        while i < n and intervals[i][1] < newInterval[0]:
            merged.append(intervals[i])
            i+=1

        while i < n and newInterval[1] >= intervals[i][0]:
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
            i+=1
        
        merged.append(newInterval)
        merged.extend(intervals[i:])
        return merged

        # old solution
        # merged = []

        # for i in range(len(intervals)):
        #     current = intervals[i]

        #     if current[1] < newInterval[0]:
        #         merged.append(current)
        #     elif current[1] >= newInterval[0] and current[0] <= newInterval[1]:
        #         merged.append([min(newInterval[0], current[0]), max(newInterval[1], current[1])])
        #         for k in range(i+1, len(intervals), 1):
        #             current = intervals[k]
        #             if merged[-1][1] < current[0]:
        #                 merged.extend(intervals[k:])
        #                 break
        #             merged[-1][1] = max(merged[-1][1], current[1])
        #         return merged
        #     elif current[0] > newInterval[1]:
        #         merged.append(newInterval)
        #         merged.extend(intervals[i:])
        #         return merged
            
        
        # merged.append(newInterval)
        # return merged

        