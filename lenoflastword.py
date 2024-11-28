class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        i = len(s)-1
        while s[i]==" ":
            i-=1
        while i>=0 and s[i]!=" ":
            count += 1
            i-=1
        return count
                
            

print(Solution().lengthOfLastWord("   fly me   to   the moon  "))
# print(Solution().lengthOfLastWord("Hello World"))
        