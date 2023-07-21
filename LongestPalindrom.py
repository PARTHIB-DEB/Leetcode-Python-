class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == '':
            return 0
        elif s == s[::-1]:
            return s
        else:
            for i in range(len(s)):
                k = 1
                if s.count(s[i])>1:
                    findex=i
                    for j in range(i+1,len(s)):
                        lindex=s.index(s[i])
                        break
            print(findex)
            print(lindex)

print(Solution().longestPalindrome("cbbd"))