class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        if len(nums)<=2 and len(set(nums))>1:
            return nums
        else:
            

print(Solution().topKFrequent([1,1,1,2,2,3],2))