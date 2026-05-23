class Solution:
    def triangleNumber(self, nums: list[int]) -> int:

        # Intuition:
        # nums.length <= 1000, and the question asked for count, so sorting wouldn't destroy and valuable information
        # in a regular triangle, we need a + b > c, a + c > b and b + c > a. But since we have a sorted array, we just need to satisfy a + b > c, since c it the largest
        # We traverse through the array, and at each index, we perform a two pointer search. Usually two pointers is for equalities, how do we use it for inequalities? 
        # In the example 1 2 4 5 6 8 9, if c=9, lp=1 and rp=8, notice this is too small so lp++. lp=2, rp=8. This works. Notice lp+rp>c will be true if we move lp to 4, 5, 6 and 8! so everything between lp in between the current lp and rp will work. 
        nums.sort()
        triplets = 0
        for i in range(2, len(nums), 1):
            left = 0
            right = i-1
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    triplets += (right - left)
                    right -= 1
                else:
                    left += 1
        return triplets



        # nums.sort()

        # triplets = 0

        # for i in range(0, len(nums)-2, 1):
        #     for k in range(1+i, len(nums)-1, 1):
        #         for r in range(1+k, len(nums), 1):
        #             if nums[i] + nums[k] > nums[r] and nums[i] + nums[r] > nums[k] and nums[r] + nums[k] > nums[i]:
        #                 triplets += 1
        # return triplets

        