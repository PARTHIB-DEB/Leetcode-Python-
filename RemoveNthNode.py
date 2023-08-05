# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n == 1:
            del_node=head
            head=del_node.next
            del_node.next=None
            # print(f"\n\t\tNODE OF VALUE: {del_node._Value} IS DELETED")
            del del_node
        else:
            i=0
            del_node=head
            while del_node is not None:
                if i==n:
                    break
                else:
                    prev=del_node # Creating Another Marker
                    del_node=del_node.next # Actual Node Marker
                    i+=1
            prev.next=del_node.next 
            del_node.next=None
            # print(f"\n\t\tNODE OF VALUE: {del_node._Value} IS DELETED")
            del del_node