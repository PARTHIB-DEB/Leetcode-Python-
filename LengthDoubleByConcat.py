class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        return nums+nums
obj=Solution()
print(obj.getConcatenation([1,2,3]))