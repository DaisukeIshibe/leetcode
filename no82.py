from typing import Optional
# Definition for singly-linked list.
# Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        current = head

		while current:
			# Check if current node has duplicates
			if current.next and current.val == current.next.val:
				# Skip all nodes with the same value
				while current.next and current.val == current.next.val:
					current = current.next
				# Link previous distinct node to the next distinct node
				prev.next = current.next
			else:
				# Move prev pointer to current if no duplicates
				prev = prev.next
			
			# Move to the next node
			current = current.next
		
		return dummy.next