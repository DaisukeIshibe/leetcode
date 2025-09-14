from typing import Optional
# Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 1. リストの長さを計算
        length = 0
        current = head
        while current:
            length += 1
            current = current.next

        # 2. k番目のノードと (length - k + 1) 番目のノードを見つける
        first_k = head
        for _ in range(k - 1):
            first_k = first_k.next

        second_k = head
        for _ in range(length - k):
            second_k = second_k.next

        # 3. ノードの値を交換
        first_k.val, second_k.val = second_k.val, first_k.val
        return head