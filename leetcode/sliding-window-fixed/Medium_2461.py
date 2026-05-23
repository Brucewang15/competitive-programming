class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        visited = {}
        cur_sum = 0
        max_sum = 0

        for i in range(k):
            visited[nums[i]] = visited.get(nums[i], 0) + 1
            cur_sum += nums[i]
        
        if len(visited.keys()) == k:
            max_sum = cur_sum

        for i in range(k, len(nums), 1):
            cur_sum += nums[i]
            cur_sum -= nums[i-k]

            visited[nums[i]] = visited.get(nums[i], 0) + 1
            visited[nums[i-k]] -= 1
            if visited[nums[i-k]] == 0:
                visited.pop(nums[i-k])
            if len(visited.keys()) == k:
                max_sum = max(max_sum, cur_sum)
        
        return max_sum
