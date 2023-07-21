class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        ans=[]
        for i in range(len(nums)):
            ans.insert(i,nums[nums[i]])
        return ans
obj=Solution()
print(obj.buildArray([0,2,1,5,3,4]))
