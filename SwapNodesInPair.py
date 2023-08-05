# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not(head and head.next):
            return head
        else:
            i=1
            temp=head
            while temp is not None:
                if i % 2 !=0:
                    del_head=head
                    head=del_head.next
                    del_head.next=None
                    res=self.swapPairs(del_head)
                    res.next=head.next
                    head=res
                temp=temp.next
                i+=1

print(Solution([1,2,3,4]))
            