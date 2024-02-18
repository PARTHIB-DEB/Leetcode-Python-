class Solution:
    def beautifulSubsets(self, nums: list[int], k: int) -> int:
        def is_beautiful(subnums):
            if len(subnums)<2:
                return True
            else:
                for i in range(len(subnums)):
                    if abs(subnums[i]-k) in subnums:
                        return False
                else:        
                    return True

        if len(nums) < 2:
            return 1
        else:
            nums.sort()
            count = 1
            for i in range(len(nums)):
                for j in range(i, len(nums)):
                    print(nums[i:j+1])
                    if is_beautiful(nums[i:j+1]):
                        count += 1
            return count

print(Solution().beautifulSubsets([4,2,5,9,10,3],1))
