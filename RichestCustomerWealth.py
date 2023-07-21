class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        return max([sum(i) for i in accounts])

print(Solution().maximumWealth([[1,2,3],[3,2,1]]))
