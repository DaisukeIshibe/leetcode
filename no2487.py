from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
		# 逆順にしてから、単調減少になるようにノードを削除
        prev = None
        curr = head
        # リストを逆順にする
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

		# 単調減少になるようにノードを削除
        new_head = None
        max_val = float('-inf')
        curr = prev

        while curr:
            if curr.val >= max_val:
                max_val = curr.val
                new_node = ListNode(curr.val)
                new_node.next = new_head
                new_head = new_node
            curr = curr.next

        return new_head