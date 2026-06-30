class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:

        mheights = [0] + heights + [0]
        areas = heights.copy()
        past = []
        for i, height in enumerate(mheights):
            while past and past[-1][1] > height:
                pi, pheight = past.pop()
                areas[pi-1] += pheight * (i - pi - 1)
            past.append((i, height))

        future = []
        for i, height in enumerate(reversed(mheights)):
            while future and future[-1][1] > height:
                fi, fheight = future.pop()
                areas[len(heights)-fi] += fheight * (i - fi - 1)
            future.append((i, height))
        return max(areas)
