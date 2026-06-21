import heapq

class Solution:
    def employeeFreeTime(self, schedule: list[list[list[int]]]) -> list[list[int]]:
        heap = []
        flattened = []
        free = []

        # methods:
        # heapq.heapify(list): o(n)
        # heapq.heappush(heap, item): log(n)
        # heapq.heappop(heap): log(n) returns smallest value and restore heap property

        # generally, heaps are used for integers. In python, heaps can be used for strings and tuples as well. For tuples, heapq will compare the first index first, then second, etc. So store priority number in the first index. 

        # o(k^2)
        # in format: (start time, employee index, employee intv index)
        for i in range(len(schedule)):
            heapq.heappush(heap, (schedule[i][0][0], i, 0))
        
        # o(nklog(k))
        while heap != []:
            _, i, ei = heapq.heappop(heap)
            flattened.append(schedule[i][ei])
            if ei < len(schedule[i]) - 1:
                heapq.heappush(heap, (schedule[i][ei+1][0], i, ei+1))

        # prev = flattened[0] means prev references the original schedule. Hence modiying prev will have side effects.
        # a better alternative is to create a new list object from the first flattened index. list() will iterate through the iterable provided and copy the array into a new object. This way no side effects.
        prev = list(flattened[0])
        for i in range(1, len(flattened), 1):
            if prev[1] < flattened[i][0]:
                free.append([prev[1], flattened[i][0]])
                prev = list(flattened[i]) # o(2). constant
            else:
                prev[1] = max(prev[1], flattened[i][1])
        return free
