from typing import Optional
# You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
#You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # リストを反転する関数
        def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
            prev = None
            current = head
            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev

        # 2つのリストを反転
        l1_reversed = reverse_list(l1)
        l2_reversed = reverse_list(l2)

        carry = 0
        dummy_head = ListNode(0)
        current = dummy_head

        # 反転したリストを足し合わせる
        while l1_reversed or l2_reversed or carry:
            val1 = l1_reversed.val if l1_reversed else 0
            val2 = l2_reversed.val if l2_reversed else 0

            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next

            if l1_reversed:
                l1_reversed = l1_reversed.next
            if l2_reversed:
                l2_reversed = l2_reversed.next

        # 結果のリストを反転して元の順序に戻す
        return reverse_list(dummy_head.next)