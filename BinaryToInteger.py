# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        to_integer = 0
        while head: 
            to_integer = 2*to_integer + head.val 
            head = head.next 
        return to_integer 