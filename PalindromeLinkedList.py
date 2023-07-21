# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head == head[::-1]:
            return True
        else:
            return False


head = [1,2,2,1]
print(Solution().isPalindrome(head))