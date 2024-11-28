class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        Step-1) Transpose the matrix
            >> Here basically the diagonal elements will be same , else if a[i][j] will be swapped with a[j][i]
        Step-2) Reverse Each row 
        """
        
        for row in range(1,len(matrix[0])):
            for col in range(row):
                matrix[row][col] , matrix [col][row] = matrix [col][row] , matrix[row][col]
        for row in range(len(matrix[0])):
            matrix[row].reverse()

mat = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
Solution().rotate(matrix=mat)
        