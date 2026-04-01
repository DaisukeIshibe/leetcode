# A binary tree is named Even-Odd if it meets the following conditions:

# The root of the binary tree is at level index 0, its children are at level index 1, their children are at level index 2, etc.
# For every even-indexed level, all nodes at the level have odd integer values in strictly increasing order (from left to right).
# For every odd-indexed level, all nodes at the level have even integer values in strictly decreasing order (from left to right).
# Given the root of a binary tree, return true if the binary tree is Even-Odd, otherwise return false.
# root = [2,12,8,5,9,null,null,18,16] Expected output: false
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        queue = [root]
        level = 0

        while queue:
            size = len(queue)
            prev_value = None

            for _ in range(size):
                node = queue.pop(0)

                # Check if the current node's value is valid for the current level
                if (level % 2 == 0 and (node.val % 2 == 0 or (prev_value is not None and node.val <= prev_value))) or (level % 2 == 1 and (node.val % 2 == 1 or (prev_value is not None and node.val >= prev_value))):
                    return False
                
                prev_value = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        return True
    