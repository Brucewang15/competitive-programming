class Solution:
    def maxArea(self, height: list[int]) -> int:

        # Max amount of water = area, which is length * height. length is k-i, while height is min(height[k], height[i]). So you can have a super long container, super tall container, or in between like a square. We need to somehow calculate all those in a smart way and take the sum. I'm thinking we start with 2 pointers, lp and rp, and gradually close them in. rp-lp will represent length. And at every step, we get the area. And we move the pointer that has a lower height, because we want to maximize height, which in turn maximizes area. And since we're reducing length, height must increase to get a larger area. Do this until lp and rp intersect, and return max_area
        max_area = 0
        lp = 0
        rp = len(height) - 1
        while lp < rp:
            max_area = max(max_area, min(height[lp], height[rp]) * (rp - lp))
            if height[lp] < height[rp]:
                lp += 1
            elif height[lp] == height[rp]:
                lp += 1
                rp -= 1
            else:
                rp -= 1
        return max_area

        # for i in range(0, len(height)-1, 1):
        #     for k in range(1+i, len(height), 1):
        #         max_vol = max(max_vol, min(height[i], height[k]) * (k-i))
        # return max_vol