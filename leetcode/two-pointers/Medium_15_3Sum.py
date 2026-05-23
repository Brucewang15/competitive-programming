class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        triplets = set()

        for i in range(0, len(nums)-2, 1):
            target = -nums[i]
            lp = i+1
            rp = len(nums)-1
            while lp < rp:
                if nums[lp] + nums[rp] == target:
                    triplets.add((-target, nums[lp], nums[rp]))
                    lp += 1
                    rp -= 1
                elif nums[lp] + nums[rp] > target:
                    rp -= 1
                else:
                    lp += 1
        return list(list(t) for t in triplets)