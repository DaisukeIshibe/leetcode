from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prefix_sum = 0
        sum_to_node = {0: dummy}
        current = head

        while current:
            prefix_sum += current.val
            if prefix_sum in sum_to_node:
                prev_node = sum_to_node[prefix_sum]
                node = prev_node.next
                temp_sum = prefix_sum

                while node != current:
                    temp_sum += node.val
                    if temp_sum in sum_to_node and sum_to_node[temp_sum] != prev_node:
                        del sum_to_node[temp_sum]
                    node = node.next

                prev_node.next = current.next
            else:
                sum_to_node[prefix_sum] = current

            current = current.next

        return dummy.next