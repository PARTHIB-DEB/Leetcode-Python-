class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<1:
            return False
        if n == 1:
            return True
        elif n % 2!=0:
            return False
        else:
            return self.isPowerOfTwo(n//2)

print(Solution().isPowerOfTwo(22))