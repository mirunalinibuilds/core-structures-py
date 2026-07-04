class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int):
        left = 0
        right = len(arr) - 1

        while right - left + 1 > k:

            left_diff = abs(arr[left] - x)
            right_diff = abs(arr[right] - x)

            if left_diff <= right_diff:
                right -= 1
            else:
                left += 1

        return arr[left:right + 1]
