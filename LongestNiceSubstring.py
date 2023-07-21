class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        sub_set = set(s)
        for i in range(len(s)):
            if s[i].lower() not in sub_set or s[i].upper() not in sub_set:
                lns1 = self.longestNiceSubstring(s[:i])
                lns2 = self.longestNiceSubstring(s[i + 1:])
                return max(lns1, lns2, key=len)
        return s
print(Solution().longestNiceSubstring("YazaAay"))