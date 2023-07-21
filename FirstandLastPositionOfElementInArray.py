class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        Index_of_Target = []
        if len(nums) >= 1:
            if nums.count(target) == 1:
                return [nums.index(target), nums.index(target)]
            elif nums.count(target)>1:
                for i in range(len(nums)):
                    if nums[i]==target:
                        Index_of_Target.append(i)
                return [Index_of_Target[0],Index_of_Target[len(Index_of_Target)-1]]
        return [-1,-1]

print(Solution().searchRange([6,6,6,8],6))
