class Solution:
    def reorganizeString(self, s: str) -> str:
        start = 0
        end  = len(s)-1
        st=""
        s=list(s)
        while start < end:
            if s[start] != s[end]:
                st+=s[start]
                st+=s[end]
                start +=1
                end -= 1
            else:
                return ""
        if len(s) % 2 != 0:
            st+=s[start]
        return st


print(Solution().reorganizeString("aab"))