from typing import List, Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        # Convert linked list to array
        linked_list_values = []
        current = head
        while current:
            linked_list_values.append(current.val)
            current = current.next

        n = len(nums)
        m = len(linked_list_values)
		
        # Create a new list to store modified values
        modified_values = []
		
        for i in range(m):
            if i < n:
                modified_values.append(linked_list_values[i] + nums[i])
            else:
                modified_values.append(linked_list_values[i])
        # Convert modified values back to linked list
        dummy_head = ListNode(0)
        current = dummy_head
        for value in modified_values:
            current.next = ListNode(value)
            current = current.next
        return dummy_head.next