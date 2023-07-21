class Solution:
    def decodeString(self, s: str) -> str:
        x=123
        list_x=list(str(x))
        print(list_x)
        y=""
        z=int(y.join(list_x))
        print(z)
        print(type(z))


s="2[abcde]"
print(Solution().decodeString(s))