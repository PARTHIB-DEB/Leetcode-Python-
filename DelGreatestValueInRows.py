class Solution:
    def deleteGreatestValue(self, grid: list[list[int]]) -> int:
        # sort each row
        for i in range(len(grid)):
            grid[i].sort(reverse=True)

        sum = 0

        # traverse through each column
        for i in range(len(grid[0])):
            maxVal = 0

            # traverse through each row
            for j in range(len(grid)):
                # get max from each row
                print(f"col={i} and row={j}")
                maxVal = max(grid[j][i], maxVal)
                print(maxVal)

            sum += maxVal

        return sum



print(Solution().deleteGreatestValue([[1,2,4],[3,3,1]]))