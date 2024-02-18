class Solution:
    def fact(self,k:int)->int:
        F=[]
        F.insert(0,1)
        F.insert(1,1)
        for i in range(2,k+1):
            F.insert(i,(i * F[i-1]))
        temp = F[k]
        del F
        return temp
        
    def numTrees(self, n: int) -> int:
        twonCn = self.fact(2*n)//self.fact(n)**2
        comb = twonCn // (n+1)
        return comb

print(Solution().numTrees(3))
        
        