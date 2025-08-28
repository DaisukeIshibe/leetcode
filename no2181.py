from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to help with the merging process
        dummy = ListNode(0)
        current = dummy
        sum = 0
        # Start from the node after the head (the first node is always 0)
        node = head.next
        while node:
            if node.val == 0:
                # If we hit a 0, we need to create a new node with the sum
                if sum > 0:
                    current.next = ListNode(sum)
                    current = current.next
                    sum = 0
            else:
                # Otherwise, keep adding to the sum
                sum += node.val
            node = node.next
        return dummy.next