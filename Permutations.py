class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        permute_list=[]
        permute_list.append(nums)
        count=0
        while(count<=len(nums)-1):
            for i in range(count+1,len(nums)):
                nums[i],nums[i+1]=nums[i+1],nums[i]
                permute_list.append(nums)
            count+=1
            nums[count]=nums[count+1]
        return list(set(nums))

print(Solution().permute([1,2,3]))
