class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '':
            return 0
        arr = []
        for i in range(len(s)):
            substring = ''
            for k in range(i, len(s)):
                if s[k] not in substring:
                    substring += s[k]
                else:
                    break
            arr.append(substring)
        return len(max(arr, key=lambda x: len(x)))





print(Solution().lengthOfLongestSubstring("abcabcbb"))
print(Solution().lengthOfLongestSubstring("bbbbb"))
print(Solution().lengthOfLongestSubstring("pwwkew"))
print(Solution().lengthOfLongestSubstring("dvdf"))