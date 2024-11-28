class Solution:
    def isHappy(self, n: int) -> bool:

        def numbysquaredigits(n:int)->int:
            res = 0
            while n > 0:
                rem = n % 10
                res += rem*rem
                n = n // 10
            return res
        
        while n > 10:
            n = numbysquaredigits(n)
        
        return n==1 or n==7 or n==10

obj = Solution()
print(obj.isHappy(int(input())))
        