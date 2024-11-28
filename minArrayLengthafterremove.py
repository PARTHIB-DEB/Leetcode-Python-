class Solution:
    def minLengthAfterRemovals(self, nums: list[int]) -> int:
        i = 0
        unused = 0
        if len(nums)<2 or len(list(set(nums)))<2:
            return len(nums)
        while i < len(nums) - 1:
            if nums[i] < nums[i+1]:
                i=i+2
            else:
                unused += 1
                i=i+1
        if len(nums[i:])==1:
            if unused>0:
                return 0
        return len(nums[i:])+unused