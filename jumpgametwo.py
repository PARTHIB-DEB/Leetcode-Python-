class Solution:
    def canJump(self, nums: list[int]) -> bool:
        # if len(nums) < 2:
        #     return True
        # elif (nums[0] == 0):
        #     return False
        # else:
        #     i = 0
        #     end = len(nums)-1
        #     while i <= end-1:
        #         if (i + nums[i]) >= end:
        #             return True
        #         elif nums[i] == 0:
        #             return False
        #         i = i + nums[i]
        #     else:
        #         return False
        for i in nums:
            print(i)


print(Solution().canJump([2,3,1,1,4]))
# print(Solution().canJump([3,2,1,0,4]))