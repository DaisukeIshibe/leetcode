# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # Find the node just before index a
        curr = list1
        for i in range(a - 1):
            curr = curr.next

        # Connect the end of list2 to the node just after index b
        tail = list2
        while tail.next:
            tail = tail.next
        tail.next = curr.next

        # Connect the node just before index a to the head of list2
        curr.next = list2

        return list1