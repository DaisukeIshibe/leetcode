"""
# Definition for a Node.
"""
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        # 1. 各ノードのコピーを作成し、元のノードの隣に挿入
        current = head
        while current:
            new_node = Node(current.val, current.next)
            current.next = new_node
            current = new_node.next
        # 2. コピーしたノードのrandomポインタを設定
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next
        # 3. 元のリストとコピーしたリストを分離
        original = head
        copy = head.next
        copy_head = head.next
        while original:
            original.next = original.next.next
            if copy.next:
                copy.next = copy.next.next
            original = original.next
            copy = copy.next
        return copy_head