import math


class Solution:
    def countPrimes(self, n: int) -> int:
        primes=[2,3,5,7]
        if 0<n<8:
            return len(primes)
        else:
            for i in range(10,n+1):
                for j in primes:
                    if i % j==0:
                        break
                else:
                    primes.append(i)
        return len(primes)

print(Solution().countPrimes(5000000))