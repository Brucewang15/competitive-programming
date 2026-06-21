class Solution:
    def employeeFreeTime(self, schedule: list[list[list[int]]]) -> list[list[int]]:
        pointers = [[i, 0, len(schedule[i]), schedule[i][0][0]] for i in range(len(schedule))]
        flattened = []
        while pointers != []:
            i, pointer, max_pointer, start = min(pointers, key=lambda x: x[3])
            flattened.append(schedule[i][pointer])
            if pointer + 1 < max_pointer:
                pointers[i][1] += 1
                pointers[i][3] = schedule[i][pointer + 1][0]
            else:
                pointers.pop(i)
        print(flattened)

        free = []

        prev = flattened[0]
        for i in range(1, len(flattened), 1):
            if prev[1] < flattened[i][0]:
                free.append([prev[1], flattened[i][0]])
                prev = flattened[i]
            else:
                prev[1] = max(prev[1], flattened[i][1])
        return free