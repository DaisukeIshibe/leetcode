from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
		num_set = set(nums)
		current = head
		count = 0
		in_component = False

		while current:
			if current.val in num_set:
				if not in_component:
					count += 1
					in_component = True
			else:
				in_component = False
			current = current.next

		return count