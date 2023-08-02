class Solution:
    def countCompleteSubarrays(self, nums: list[int]) -> int:
        if len(set(nums))==1:
            for i in nums:
                return 2*i
        else:
            subarray=[]
            subarray.append(nums)
            for i in range(len(nums)):
                part_sub=nums[i:]
                if part_sub not in subarray and set(part_sub) == set(nums):
                    subarray.append(part_sub)
            return subarray

print(Solution().countCompleteSubarrays([1,3,1,2,2]))
        
        
        