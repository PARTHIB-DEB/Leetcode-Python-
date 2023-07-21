class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        nums=list(set(nums))
        min_len = 1
        if target>=max(nums):
            for i in nums:
                if target in nums:
                    return min_len
                else:
                    self.minSubArrayLen(target-i,nums)
                    min_len+=1
        return 0


print(Solution().minSubArrayLen(11,[1,2,3,4,5]))