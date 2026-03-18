from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        root.val = 0
        queue = [root]

        while queue:
            next_level = []
            next_level_sum = 0

            for node in queue:
                if node.left:
                    next_level.append(node.left)
                    next_level_sum += node.left.val
                if node.right:
                    next_level.append(node.right)
                    next_level_sum += node.right.val

            for node in queue:
                sibling_sum = 0
                if node.left:
                    sibling_sum += node.left.val
                if node.right:
                    sibling_sum += node.right.val

                if node.left:
                    node.left.val = next_level_sum - sibling_sum
                if node.right:
                    node.right.val = next_level_sum - sibling_sum

            queue = next_level

        return root