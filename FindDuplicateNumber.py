class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        if len(nums)<2:
            return
        else:
            p1 , p2 = 0 , 0
            while True:
                p1 ,p2 = nums[p1] , p2[nums[p2]]
                if p1 == p2:
                    break
            print(nums[p2])
            return nums[p2]

Solution().findDuplicate([1,3,4,2,2])
Solution().findDuplicate([3,1,3,4,2])