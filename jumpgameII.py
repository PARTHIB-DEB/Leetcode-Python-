class Solution:
    def jump(self, nums: list[int]) -> int:
        count=0
        l,root=0,0
        while root <len(nums)-1 :
            farthest=0
            for i in range(l,root+1):
                farthest=max(farthest,i +nums[i])
            l=root+1
            root=farthest
            count +=1
        return count

Solution().jump([1,2,3])
print("\n\n")
Solution().jump([2,3,0,1,4])