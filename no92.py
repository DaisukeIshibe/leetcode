from types import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        # Create a dummy node to simplify edge cases
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # Move `prev` to the node before the reversal
        for _ in range(left - 1):
            prev = prev.next

        # Start reversing the sublist
        curr = prev.next
        tail = curr
        for _ in range(right - left + 1):
            next_node = curr.next
            curr.next = prev.next
            prev.next = curr
            curr = next_node

        # Connect the reversed sublist back to the original list
        tail.next = curr

        return dummy.next