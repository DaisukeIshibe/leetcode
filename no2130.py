from types import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: 'ListNode') -> int:
        vals = []
        node = head
        while node:
            vals.append(node.val)
            node = node.next
        max_sum = 0
        n = len(vals)
        for i in range(n // 2):
            max_sum = max(max_sum, vals[i] + vals[n - 1 - i])
        return max_sum