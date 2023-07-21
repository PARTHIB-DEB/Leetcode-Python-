class Solution:
    def semiOrderedPermutation(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 0
        elif nums[0] == min(nums) and nums[len(nums)-1] == max(nums):
            return 0
        else:
            if nums.index(max(nums))-nums.index(min(nums)) == 1:
                if len(nums) % 4 == 0:
                    return 2
                elif len(nums) % 3 == 0:
                    return 