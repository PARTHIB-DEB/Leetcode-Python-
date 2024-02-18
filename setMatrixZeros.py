class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return []
        rows, cols = len(matrix),len(matrix[0])
        row_index , col_index = [-1]*rows , [-1]*cols
        for row in range(rows):
             for col in range(cols):
                 if matrix[row][col] == 0:
                    row_index[row] = 0
                    col_index[col] = 0

        for row in range(rows):
            for col in range(cols):
                if row_index[row]==0 or col_index[col]==0:
                    matrix[row][col] = 0