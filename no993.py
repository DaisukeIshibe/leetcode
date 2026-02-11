from collections import deque
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root:
            return False
        
        queue = deque([(root, 0, None)])  # (node, depth, parent)
        x_info = y_info = None
        
        while queue:
            node, depth, parent = queue.popleft()
            
            if node.val == x:
                x_info = (depth, parent)
            elif node.val == y:
                y_info = (depth, parent)
            
            if x_info and y_info:
                break
            
            if node.left:
                queue.append((node.left, depth + 1, node))
            if node.right:
                queue.append((node.right, depth + 1, node))
        
        if x_info and y_info:
            return x_info[0] == y_info[0] and x_info[1] != y_info[1]
        
        return False