class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = [[]]
        for num in nums:
            newArr = []
            for item in res:
                newArr.append(item + [num])
            res += newArr
        return res

print(Solution().subsets([1,2,3]))