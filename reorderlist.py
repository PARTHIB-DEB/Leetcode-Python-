class Node:
    def __init__(self,val=0,next=None) -> None:
        self.val = val
        self.next = next

class Solution:
    def __init__(self) -> None:
        self.head = Node()
        
    def fillvalue(self,headlist:list):
        temp=self.head
        for i in range(len(headlist)-1):
            temp.val=headlist[i]
            temp.next = Node()
            temp=temp.next
        temp.val=headlist[len(headlist)-1]
        temp.next = None
        return self.head
    
    def reorderList(self, headlist:list) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        curr = self.fillvalue(headlist=headlist)
        left = curr
        right = curr.next
        while curr and right:
            left = left.next
            right = left
                


Solution().reorderList([1,2,3,4])
            