from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        queue = [root]
        end = False

        while queue:
            node = queue.pop(0)

            if node:
                if end:
                    return False
                queue.append(node.left)
                queue.append(node.right)
            else:
                end = True

        return True