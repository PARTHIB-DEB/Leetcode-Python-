class Solution:
    def findNonMinOrMax(self, nums: list[int]) -> int:
        if len(nums) > 1:
            nums.remove(min(nums))
            nums.remove(max(nums))
            if len(nums) >= 1:
                return min(nums)
            else:
                return -1
        else:
            return -1

obj=Solution()
response = obj.findNonMinOrMax([3,2,1,4])
print(response)