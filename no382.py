from typing import Optional
# Definition for singly-linked list.
# Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self, head: Optional[ListNode]):
        import random
        self.head = head
        self.size = 0
        node = head
        while node:
            self.size += 1
            node = node.next
        self.random = random.Random()
        self.random.seed()
        self.node_dict = {}
        node = head
        for i in range(self.size):
            self.node_dict[i] = node.val
            node = node.next
                        
    def getRandom(self) -> int:
        rand_index = self.random.randint(0, self.size - 1)
        return self.node_dict[rand_index]


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()