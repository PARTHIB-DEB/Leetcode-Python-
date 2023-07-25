class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        left_indices=right_indices=[]
        for i in range(len(s)):
            if s[i]=="(":
                left_indices.append(i)
            elif s[i]==")":
                right_indices.append(i)
        print(left_indices)
        print(right_indices)

print(Solution().minAddToMakeValid("())"))
