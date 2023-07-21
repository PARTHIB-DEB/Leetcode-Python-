class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count=0
        letter_count_s_t=dict()
        for i in set(s):
            letter_count_s_t[i]=s.count(i)-t.count(i)
            if s.count(i)-t.count(i)>0:
                count+=s.count(i)-t.count(i)
        return count


print(Solution().minSteps("anagram","mangaar"))
