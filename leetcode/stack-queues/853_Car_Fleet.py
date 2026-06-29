class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        merged = list(zip(position, speed))
        merged.sort(key=lambda x: x[0])
        stack = []
        for (pos, s) in merged:
            while stack and stack[-1][1] > s:
                time = (target - pos) / s
                if stack[-1][0] + stack[-1][1] * time >= target:
                    stack.pop()
                else:
                    break
            stack.append((pos, s))
        return len(stack)
        # for (pos, s) in merged:
        #     t = 0
        #     while stack and stack[-1][1] > s:
        #         ppos, ps, pt = stack[-1]
        #         time_to_merge = (pos - (ppos + ps * (t - pt))) / (ps - s)
        #         if pos + time_to_merge * s <= target:
        #             pos, s, t = pos + time_to_merge * s, s, time_to_merge + t
        #             stack.pop()
        #         else:
        #             break
        #     stack.append((pos, s, t))

        # return len(stack)