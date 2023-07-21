class Solution:
    def repeatedCharacter(self, s: str) -> str:
        list_s = []
        for i in range(len(s)):
            if s[i] in list_s:
                return s[i]
            else:
                list_s.append(s[i])

print(Solution().repeatedCharacter("abccbaacz"))