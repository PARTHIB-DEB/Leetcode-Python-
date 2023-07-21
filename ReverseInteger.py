import math


class Solution:
    def reverse(self, x: int) -> int:
        if (-1)*math.pow(2,31)<=x<=math.pow(2,31)-1:
            if x > 0:
                str_x = str(x)
                return int("".join(str_x[::-1]))
            else:
                str_x = str(abs(x))
                return (-1) * int("".join(str_x[::-1]))
        else:
            return 0

print(Solution().reverse(-123))