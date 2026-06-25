class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0

        window_sum = sum(arr[:k])

        if window_sum >= threshold * k:
            count += 1

        for right in range(k, len(arr)):

            window_sum = window_sum - arr[right-k] + arr[right]

            if window_sum >= threshold * k:
                count += 1

        return count
