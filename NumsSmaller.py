class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        count_nums=[]
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if i!=j and nums[i]>nums[j]:
                    count+=1
            else:
                count_nums.append(count)
        return count_nums
print(Solution().smallerNumbersThanCurrent([8,1,2,2,3]))