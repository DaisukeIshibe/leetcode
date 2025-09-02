from types import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # Initialize pointers
        prev = None
        curr = head

        # Swap pairs
        while curr and curr.next:
            next_pair = curr.next.next
            curr.next.next = curr
            if prev:
                prev.next = curr.next
            else:
                head = curr.next
            curr.next = next_pair
            prev = curr
            curr = next_pair

        return head