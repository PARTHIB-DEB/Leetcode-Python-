class Solution:
    def isPalindrome(self, s: str) -> bool:
        # if s.isspace()==True:
        #     return True
        # else:
        #     s = [char.lower() for char in s if char.isalnum()]
        #     return s == s[::-1]
        s = [char.lower() for char in s if char.isalnum()]
        print(s)


print(Solution().isPalindrome("A man, a plan, a canal: Panama"))