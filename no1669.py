# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # a-1番目のノードを探す
        prev_a = list1
        for _ in range(a - 1):
            prev_a = prev_a.next

        # b番目のノードを探す
        after_b = prev_a
        for _ in range(b - a + 2):
            after_b = after_b.next

        # list2の末尾を探す
        tail = list2
        while tail.next:
            tail = tail.next

        # つなぎ替え
        prev_a.next = list2
        tail.next = after_b

        return list1