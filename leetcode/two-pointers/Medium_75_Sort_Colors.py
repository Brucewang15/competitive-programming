class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        p0 = 0
        p2 = len(nums) - 1
        i = 0

        while i <= p2:
            if nums[i] == 0:
                nums[i] = nums[p0]
                nums[p0] = 0
                p0 += 1
            elif nums[i] == 2:
                nums[i] = nums[p2]
                nums[p2] = 2
                p2 -= 1
                i -= 1
            i += 1


        # lp = 0
        # l_nums = len(nums)
        # for i in range(3):
        #     for k in range(lp, l_nums, 1):
        #         if nums[k] == i:
        #             nums[k] = nums[lp]
        #             nums[lp] = i
        #             lp += 1