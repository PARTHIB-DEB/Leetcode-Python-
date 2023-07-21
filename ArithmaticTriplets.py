class Solution:
    def arithmeticTriplets(self, nums: list[int], diff: int) -> int:
        '''
        i<j<k
        nums[j] - nums[i] == diff
        nums[k] - nums[j] == diff
        --------------------------
        nums[j] and nums[k] proportional to nums[i] by 'diff'
        '''
        j_list=list()
        pair_count=0
        for x in range(len(nums)):
            j_list.insert(x,diff+nums[x])
        num_dict=dict(enumerate(nums))
        for key in num_dict.keys():
            if num_dict[key] in j_list:
                if 0<key<

                    count = 0
                    n = len(nums)
                    for i in range(n - 2):
                        for j in range(i + 1, n - 1):
                            if nums[j] - nums[i] == diff:
                                for k in range(j + 1, n):
                                    if nums[k] - nums[j] == diff:
                                        count += 1
                    return count

print(Solution().arithmeticTriplets([0,1,4,6,7,10],3))
print(Solution().arithmeticTriplets([4,5,6,7,8,9],2))