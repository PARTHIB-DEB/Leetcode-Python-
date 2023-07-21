class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        hash = {}
        for index, num in enumerate(nums):
            if num in hash and index - hash[num] <= k:
                return True
            hash[num] = index
        return False
# print(Solution().containsNearbyDuplicate([1,2,3,1],3))
print(Solution().containsNearbyDuplicate([1,2,3,1,2,3],2))