import functools
class Solution:
    def romanToInt(self, s: str) -> int:
        my_dict={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        my_list=list(s)
        for i in range(len(my_list)):
            my_list[i]=my_dict[my_list[i]]
        print(my_list)
obj=Solution()
obj.romanToInt(input())