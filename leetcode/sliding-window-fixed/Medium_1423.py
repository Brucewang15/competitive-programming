class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        k_rev = len(cardPoints) - k
        total_points = sum(cardPoints)

        cur_min = 0
        for i in range(k_rev):
            cur_min += cardPoints[i]
        
        min_sum = cur_min

        for i in range(k_rev, len(cardPoints), 1):
            cur_min += cardPoints[i]
            cur_min -= cardPoints[i-k_rev]

            min_sum = min(min_sum, cur_min)
        
        return total_points - min_sum
        