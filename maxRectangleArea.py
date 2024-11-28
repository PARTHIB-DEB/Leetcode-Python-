class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        if len(matrix)==1:
            if len(matrix[0])==1:
                return int(matrix[0][0])
        else:
            row_col_dict={}
            for i in range(len(matrix)):
                cols = 0
                for j in range(1,len(matrix[i])):
                    if matrix[i][j-1] == matrix[i][j] and matrix[i][j]=="1":
                        cols +=1
                if cols>0:
                    row_col_dict[i]=cols+1
            return(len(row_col_dict.keys())*min(row_col_dict.values()))

matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Solution().maximalRectangle(matrix)





