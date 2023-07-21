class Solution:
    def mostFrequentEven(self, nums: list[int]) -> int:
        repeat_count=set()
        for i in nums:
            if i % 2 ==0 and nums.count(i)>1:
                repeat_count.add(i)
        repeat_list=list(repeat_count)
        return repeat_list[0]


print(Solution().mostFrequentEven([0,1,2,2,4,4,1]))