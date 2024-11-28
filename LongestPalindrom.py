# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         if s == '':
#             return s[0]
#         elif s==s[::-1]:
#             return s
#         else:
#             '''
#             Rules:
#             1. Find Element/s which is occuring More Times.
#             2. Capture Those elements in a set and mark its length in a variable
#             3. Get the Index of one element of that set in the string
#             4. Run a Loop on the string where if the element from the set matches 2 times , then return the pal-string
#             '''
#             list_s = list(s)
#             pal_strings = []
#             flag  = 0
#             for i in range(len(list_s)):
#                 if list_s.count(list_s[i])>1:
#                     item = list_s[i]
#                     flag = 1
#                     for j in range(i+1,len(list_s)):
#                         if list_s[j] == item:
#                             pal_strings.append(s[i:j+1])
#             if flag == 0:
#                 return s[0]
#             else:
#                 # return pal_strings[0]
#                 print (pal_strings)

# # Solution().longestPalindrome("babad")
# # Solution().longestPalindrome("cbbd")
# # Solution().longestPalindrome("ac")
# Solution().longestPalindrome("aacabdkacaa")

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        def expand_from_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        max_str = s[0]

        for i in range(len(s) - 1):
            odd = expand_from_center(i, i)
            even = expand_from_center(i, i + 1)

            if len(odd) > len(max_str):
                max_str = odd
            if len(even) > len(max_str):
                max_str = even

        return max_str