class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        count = 0
        for i in range(len(nums)):
            if i == len(nums) - 1:
                return count
            else:
                for j in range(i + 1, len(nums)):
                    if nums[i] == nums[j]:
                        count += 1
print(Solution().numIdenticalPairs([1,2,3,1,1,3]))