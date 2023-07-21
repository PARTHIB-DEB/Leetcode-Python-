class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        j_count=0
        for i in range(len(jewels)):
            j_count+=stones.count(jewels[i],0,len(stones))
        return  j_count

print(Solution().numJewelsInStones("aA","aAAbbbb"))