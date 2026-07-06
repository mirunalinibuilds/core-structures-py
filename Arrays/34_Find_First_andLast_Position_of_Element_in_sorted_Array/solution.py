class Solution:
    def searchRange(self, nums: List[int], target: int):

        left = 0
        right = len(nums) - 1

        first_occur = -1
        last_occur = -1

        # Find first occurrence
        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:
                first_occur = mid
                right = mid - 1

            elif nums[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        # Reset pointers
        left = 0
        right = len(nums) - 1

        # Find last occurrence
        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:
                last_occur = mid
                left = mid + 1

            elif nums[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return [first_occur, last_occur]
