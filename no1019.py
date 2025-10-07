from typing import List, Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        # Convert linked list to array
        values = []
        while head:
            values.append(head.val)
            head = head.next

        # Find next larger nodes
        result = [0] * len(values)
        stack = []
        for i, value in enumerate(values):
            while stack and values[stack[-1]] < value:
                result[stack.pop()] = value
            stack.append(i)

        return result
