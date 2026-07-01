class Solution:
    def f(self, nums, i):
        if nums[i] >= nums[0]:
            return 0
        return 1
    def search(self, nums: list[int], target: int) -> int:
        k = 0
        if nums[0] > nums[-1]:
            left, right = 0, len(nums) - 1
            while left < right:
                mid = (left + right + 1) // 2
                if self.f(nums, mid) == 0:
                    left = mid
                else:
                    right = mid - 1
            k = right + 1

        left, right = 0, len(nums) - 1
        while left <= right:
            fmid = (left + right) // 2
            rmid = (((left + right) // 2) + k) % len(nums)
            if nums[rmid] == target:
                return rmid
            elif nums[rmid] > target:
                right = fmid - 1
            else:
                left = fmid + 1
        return -1