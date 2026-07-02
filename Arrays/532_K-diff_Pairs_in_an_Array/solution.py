class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:

        if k < 0:
            return 0

        count = 0

        if k > 0:

            seen = set(nums)

            for num in seen:
                if num + k in seen:
                    count += 1

            return count

        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for value in freq.values():
            if value >= 2:
                count += 1

        return count
