class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        lp = 0

        for num in nums:
            if num != 0:
                nums[lp] = num
                lp += 1
        for i in range(lp, len(nums), 1):
            nums[lp] = 0
            lp += 1




        # moveTo = 0
        # for num in nums:
        #     if num != 0:
        #         nums[moveTo] = num
        #         moveTo += 1
        # for i in range(moveTo, len(nums), 1):
        #     nums[i] = 0
        # return nums

        # moveTo = 0

        # for i in range(len(nums)):
        #     if nums[i] != 0:
        #         temp = nums[moveTo]
        #         nums[moveTo] = nums[i]
        #         nums[i] = temp
        #         moveTo += 1
        # return nums