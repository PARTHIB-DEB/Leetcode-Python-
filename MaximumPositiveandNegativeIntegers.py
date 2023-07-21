class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        pos=[]
        neg=[]
        for i in nums:
            if i>0:
                pos.append(i)
            if i<0:
                neg.append(i)
        return max(len(pos),len(neg))