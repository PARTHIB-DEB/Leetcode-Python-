class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        i , j = 1 , len(nums)-2
        start , end = 0 , len(nums)-1
        indexlist = []
        while i <j:
            if sum(nums[start:i]) < sum(nums[i:end+1]):
                val = i*10+end
                indexlist.append(val)
            else:
                val = start*10 + i-1
                indexlist.append(val)
            if sum(nums[j:end]) < sum(nums[start:j+1]):
                val = i*10+j
                indexlist.append(val)
            else:
                val = start*10+end-1
                indexlist.append(val)
            i+=1
            j-=1
        max_index_pair = max(indexlist)
        start = max_index_pair//10
        end = max_index_pair%10
        # return sum(nums[start:end+1])
        print(f"Start : {nums[start]} , end : {nums[end]} , sum = {sum(nums[start:end+1])}")

print(Solution().maxSubArray([1,2,-1,10,4,1,-1]))
        
                
        