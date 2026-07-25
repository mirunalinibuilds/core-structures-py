class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        window_sum = sum(nums[:k])
        ans = window_sum

        for right in range(k, len(nums)):
            window_sum = window_sum + nums[right] - nums[right - k]
            ans = max(ans, window_sum)

        return ans / k
