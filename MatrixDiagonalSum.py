class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        if len(mat) == 1:
            return mat[0][0]
        elif len(mat) % 2 != 0:
            row = forward_col = 0
            backward_col = temp = len(mat) - 1
            odd_diagonals = []
            # For odd x odd matrix there must be one centre element , first capture that
            odd_diagonals.append(mat[backward_col // 2][backward_col // 2])
            # Remember Here Row is not the main factor , but the main factor is the two column_counters
            while (forward_col < backward_col):
                odd_diagonals.append(mat[row][forward_col])
                odd_diagonals.append(mat[row][backward_col])
                forward_col += 1
                backward_col -= 1
                row += 1  # Here row is temp//2 now , but at this row , the value is already taken so
            row += 1  # Again increment it
            # After Half length sliding, when the row furthur needs to increase then we have to set a condition for that
            # Along with repositioning the two column sliders backwards
            while (forward_col >= 0 and backward_col <= temp and row <= temp):
                forward_col -= 1
                odd_diagonals.append(mat[row][forward_col])
                backward_col += 1
                odd_diagonals.append(mat[row][backward_col])
                row += 1
            return sum(odd_diagonals)
        else:
            row = forward_col = 0
            backward_col = temp = len(mat) - 1
            mid_col_negative = (temp - 1) // 2
            mid_col_positive = (temp + 1) // 2
            even_diagonals = []
            # For even x even matrix there must be 4 centre element , first capture those
            even_diagonals.append(mat[mid_col_negative][mid_col_negative])
            even_diagonals.append(mat[mid_col_negative][mid_col_positive])
            even_diagonals.append(mat[mid_col_positive][mid_col_positive])
            even_diagonals.append(mat[mid_col_positive][mid_col_negative])
            # Remember Here Row is not the main factor , but the main factor is the two column_counters
            while (forward_col < backward_col - 2 and row <= mid_col_negative):
                even_diagonals.append(mat[row][forward_col])
                even_diagonals.append(mat[row][backward_col])
                forward_col += 1
                backward_col -= 1
                row += 1
            row += 1
            # After Half length sliding, when the row furthur needs to increase then we have to set a condition for that
            # Along with repositioning the two column sliders backwards
            while (row < temp):
                row += 1
                forward_col -= 1
                backward_col += 1
                even_diagonals.append(mat[row][forward_col])
                even_diagonals.append(mat[row][backward_col])
            return sum(even_diagonals)


mat=[[1,2,3],[4,5,6],[7,8,9]]
print(Solution().diagonalSum(mat))
mat = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]
print(Solution().diagonalSum(mat))
mat =[[7,3,1,9],[3,4,6,9],[6,9,6,6],[9,5,8,5]]
print(Solution().diagonalSum(mat))
