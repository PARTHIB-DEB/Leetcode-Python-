# class Solution:
#     def candy(self, ratings: list[int]) -> int:
#         '''
#         1.Suppose The Ratings is in Increasing order then if ratings[i-1]<ratings[i],arr[i]=arr[i-1]+1
#         2.Otherwise check with 1 and then check from reverse
#         '''
#         arr = [1]*len(ratings)
#         for i in range(1,len(ratings)):
#             if ratings[i-1]<ratings[i]:
#                 arr[i]=arr[i-1]+1
#         for i in range(len(ratings)-2,-1,-1):
#             if ratings[i]>ratings[i+1]:
#                 arr[i] = max(arr[i],arr[i+1]+1)
                
#         return sum(arr)

# # print(Solution().candy([1,0,2]))
# # print(Solution().candy([1,2,2]))
# print(Solution().candy([1,2,87,87,87,2,1]))

print(set([9,1,2,5,8,3]) set([3,4,6,5]))