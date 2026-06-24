class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])

        row_sums = [0] * rows
        col_sums = [0] * cols

        for i in range(rows):
            for j in range(cols):
                row_sums[i] += mat[i][j]
                col_sums[j] += mat[i][j]

        count = 0

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 1 and row_sums[i] == 1 and col_sums[j] == 1:
                    count += 1

        return count
