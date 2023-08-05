# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        backbone = ListNode()
        prefix, prev = 0, backbone
        while head:
            if head.val == 0:
                if prefix > 0:
                    prev.next = ListNode(prefix)
                    prefix = 0
                    prev = prev.next
            else:
                prefix += head.val
            head = head.next
        return backbone.next
                
print(Solution().mergeNodes([0,3,1,0,4,5,2,0]))