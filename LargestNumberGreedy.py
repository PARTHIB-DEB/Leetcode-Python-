import functools
class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        if len(nums) < 2:
            return str(nums[0])
        else:
            def cmp_nums(s1,s2):
                if s1+s2 > s2+s1:
                    return -1
                else:
                    return 1
            nums=[str(num)for num in nums]
            nums = sorted(nums,key=functools.cmp_to_key(cmp_nums))
            return str(int("".join(nums)))

Solution().largestNumber([1,2,3])
Solution().largestNumber([10,2])
Solution().largestNumber([3,30,34,5,9])