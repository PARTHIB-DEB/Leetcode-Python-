from collections import Counter
from itertools import zip_longest


class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        #  Example: [1,3,4,1,2,3,1]

        c = Counter(nums)  # c = {1:3, 3:2, 4:1, 2:1})

        ans = zip_longest(*[[k] * c[k] for k in c])  # ans = zip_longest([1,1,1],[3,3],[4],[2])
        #      = [(1, 3, 4, 2), (1, 3, None, None), (1, None, None, None)]

        return list(map(lambda x: [n for n in x if n], ans))  # ans = [[1, 3, 4, 2], [1, 3], [1]]

print(Solution().findMatrix([1,3,4,1,2,3,1]))