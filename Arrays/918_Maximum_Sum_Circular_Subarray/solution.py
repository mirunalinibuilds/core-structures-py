class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        current_min_sum = nums[0]
        current_max_sum = nums[0]

        min_sum = nums[0]
        max_sum = nums[0]

        total = sum(nums)

        for i in range(1, len(nums)):

            current_min_sum = min(current_min_sum + nums[i], nums[i])
            min_sum = min(current_min_sum, min_sum)

            current_max_sum = max(current_max_sum + nums[i], nums[i])
            max_sum = max(current_max_sum, max_sum)

        if max_sum < 0:
            return max_sum

        return max(max_sum, total - min_sum)
