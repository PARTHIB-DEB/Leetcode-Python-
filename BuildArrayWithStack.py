class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        '''
        In this problem,
        1) Fill the stack with either "push" or "pop"
        2) the two P's are the stack operations to make a array --> given target array
        3) To fill the array we have to do the two P's on a stream of integers 1 to n
        '''
        operations=[]
        for i in range(1,n+1):
            if i in target:
                operations.append("Push")
            else:
                operations.append("Push")
                operations.append("Pop")
            if i == target[-1]:
                return operations
            
print(Solution().buildArray([1,3],3))