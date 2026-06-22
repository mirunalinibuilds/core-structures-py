class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0

        for row in grid:

            left = 0
            right = len(row) - 1
            answer = -1

            while left <= right:

                mid = (left + right) // 2

                if row[mid] < 0:
                    answer = mid
                    right = mid - 1

                else:
                    left = mid + 1

            if answer == -1:
                total_negatives_of_row = 0
            else:
                total_negatives_of_row = len(row) - answer

            count += total_negatives_of_row

        return count
