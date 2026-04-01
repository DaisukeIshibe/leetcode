from typing import List, Optional

# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = [root]

        while queue:
            level_size = len(queue)
            level_values = []

            for _ in range(level_size):
                node = queue.pop(0)
                level_values.append(node.val)

                if node.children:
                    queue.extend(node.children)

            result.append(level_values)

        return result