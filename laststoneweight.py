class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        if len(stones) ==1 :
            return stones[0]
        while len(stones) > 1 :
            stones.sort(reverse=True)
            l1,l2 = stones[0] , stones[1]
            stones.remove(l1)
            stones.remove(l2)
            if l1 > l2:
                stones.append(l1-l2) 
        return stones[0]

print(Solution().lastStoneWeight([1,3]))