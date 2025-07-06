from typing import Optional
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
          self.val = val
          self.next = next
	

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr_node = head

        while curr_node is not None:
            next_node = curr_node.next
            curr_node.next = prev
            prev = curr_node
            curr_node = next_node
        return prev

sol = Solution()
print(f'{sol.reverseList([1, 2, 3, 4, 5])} expect [5, 4, 3, 2, 1]') # Expect None