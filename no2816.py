from typing import Optional
'''
You are given the head of a non-empty linked list representing a non-negative integer without leading zeroes.

Return the head of the linked list after doubling it.
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            prev = None
            curr = head
            while curr:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev

        head = reverse(head)
        carry = 0
        curr = head

        while curr:
            total = curr.val * 2 + carry
            curr.val = total % 10
            carry = total // 10

            if not curr.next and carry:
                curr.next = ListNode(carry)
                carry = 0  # キャリーをリセット
            
            curr = curr.next
        
        return reverse(head)

sol = Solution()
print(f'{sol.doubleIt(ListNode(1, ListNode(8, ListNode(9)))).val} expect [3,7,8]')