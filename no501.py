from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        stack = []
        current = root
        prev_val = None
        current_count = 0
        max_count = 0
        modes = []

        while stack or current:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()

            if prev_val is None or current.val != prev_val:
                current_count = 1
            else:
                current_count += 1

            if current_count > max_count:
                max_count = current_count
                modes = [current.val]
            elif current_count == max_count:
                modes.append(current.val)

            prev_val = current.val
            current = current.right

        return modes